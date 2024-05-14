def collatz(number):
    return number // 2 if number % 2 == 0 else 3 * number + 1

def main():
    try:
        n = int(input("整数を入力してください: "))
        if n <= 0:
            raise ValueError
        while n != 1:
            n = collatz(n)
            print(n)
    except ValueError:
        print("正の整数を入力してください。")

if __name__ == "__main__":
    main()

