def split_bill(price):
    num = input('何にんで割り勘しますか？')
    try:
        each = price / int(num)
    except:
        print('エラーが発生しました。正しい値を入力してください。')
        each = price
    print(f'一人{each}円です')

if __name__ == "__main__":
    split_bill(10000)