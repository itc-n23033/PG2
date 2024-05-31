import pyinputplus as pyip

while True:
    prompt = 'バカを何時間も忙しくせせておく方法を知りたいですか？\n'
    response = pyip.inputYesNo(prompt)

    if response == 'no':
        break

    print('ありがとう、ごきげんよう。')

    response = pyip.inputYesNo(prompt, yesVal='はい', noVal='いいえ')
    if response == 'いいえ':
        break
