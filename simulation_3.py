import random

coin100 = 0
min_coin100 = 0
required100 = 0

coin500 = 0
min_coin500 = 0
required500 = 0

# input関数を使って任意の割合を入力する
rate_200 = float(input("200円の割合を入力してください（例： 0.4）："))
rate_500 = float(input("500円の割合を入力してください（例： 0.3）："))
rate_1000 = 1.0 - rate_200 - rate_500

for i in range(1, 51):
    rn = random.random()
    if rn < rate_200:
        pay = "200円"
        coin100 += 2
    elif rate_200 <= rn < rate_200 + rate_500:
        pay = "500円"
        coin500 += 1
        # 釣り銭に100円玉があるとき
        if coin100 >= 3:
            coin100 -= 3
        # 釣り銭がないとき
        else:
            required100 -= 3
    else:
        pay = "1000円"
        # 釣り銭に500円玉と100円玉があるとき
        if coin500 >= 1 and coin100 >= 3:
            coin500 -= 1
            coin100 -= 3
        # 釣り銭に100円玉があるとき
        elif coin100 >= 8:
            coin100 -= 8
        # 釣り銭がないとき
        else:
            required500 -= 1
            required100 -= 3

    print(
        f"{i}人目:{pay}:【在庫枚数：100円玉は{coin100}枚、500円玉は{coin500}枚】 【不足枚数：100円玉は{required100}枚、500円玉は{required500}枚】"
    )

# 100円玉、500円玉の在庫枚数を不足枚数に補充
required100 += coin100
if required100 < min_coin100:
    min_coin100 = required100
required500 += coin500
if required500 < min_coin500:
    min_coin500 = required500

print(
    f"{'-'*30}\n"
    f"○ 200円の割合：{rate_200}\n"
    f"◎ 500円の割合：{rate_500}\n"
    f"● 1000円の割合：{rate_1000:.1f}\n"
    f"上記の場合のシミュレーション\n"
    f"100円玉の最大不足枚数:{abs(min_coin100)}枚\n"
    f"500円玉の最大不足枚数:{abs(min_coin500)}枚\n"
    f"{'-'*30}\n"
)
