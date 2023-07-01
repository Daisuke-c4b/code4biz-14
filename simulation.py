import random

coin100 = 0
coin500 = 0
bill1000 = 0
min_coin = 0
for i in range(1, 51):
    rn = random.random()
    # if rn < 0.5: # 課題2-1 200円 / 500円 = 50% / 50%
    # if rn < 0.9: # 課題2-2 200円 / 500円 = 90% / 10%
    # if rn < 0.1: # 課題2-3 200円 / 500円 = 10% / 90%
    # if rn < 0.4: # 課題3-1 200円 / 500円 / 1000円 = 40% / 30% / 30%
    # if rn < 0.8: # 課題3-2 200円 / 500円 / 1000円 = 80% / 10% / 10%
    if (
        rn < 0.5
    ):  # 課題4   200円 / 500円 / 1000円 / 5000円 / 10000円 = 50% / 30% / 10% / 8% / 2%
        pay = "200円"
        coin100 += 2
    elif 0.5 <= rn < 0.8:
        pay = "500円"
        coin500 += 1
    elif 0.8 <= rn < 0.9:
        pay = "1000円"
        bill1000 += 1
        if coin500 > 0:
            coin500 -= 1
            coin100 -= 3
        else:
            coin100 -= 8
    elif 0.9 <= rn < 0.98:
        pay = "5000円"
        if bill1000 > 3:  # 4枚
            bill1000 -= 4
            coin500 -= 1
            coin100 -= 3
        elif bill1000 > 2:  # 3枚
            bill1000 -= 4
            coin500 -= 1
            coin100 -= 3
        else:
            coin100 -= 8
    else:
        pay = "10000円"
        if coin500 > 0:
            coin500 -= 1
            coin100 -= 3
        else:
            coin100 -= 8
    print(f"{i}人目:{pay}:100円玉は{coin100}枚、500円玉は{coin500}枚")
    if coin100 < min_coin:
        min_coin = coin100

print(f"100円玉の最大不足枚数:{abs(coin100)}枚")
