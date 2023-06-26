import random

coin = 0
min_coin = 0
for i in range(1, 51):
    rn = random.random()
    if rn < 0.5:
        pay = "200円"
        coin = coin + 2
    else:
        pay = "500円"
        coin = coin - 3
    print(f"{i}人目:{pay}:100円玉は{coin}枚")
    if coin < min_coin:
        min_coin = coin
print(f"最大不足枚数は{abs(min_coin)}枚")
