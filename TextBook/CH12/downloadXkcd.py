import bs4, os, requests

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)  # ./xkcdフォルダを作成する

while not url.endswith('#'):
    # ページをダウンロードする
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # コミック画像のURLを見つける
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('Could not find comic image.')
    else:
        comic_url = 'http:' + comic_elem[0].get('src')
        # 画像をダウンロードする
        print(f'Downloading image {comic_url}...')
        res = requests.get(comic_url)
        res.raise_for_status()

        # 画像を./xkcdに保存する
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

    # PrevボタンのURLを取得する
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print('完了')