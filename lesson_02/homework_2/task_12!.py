coins = int(input("Количество монет у Учителя: "))
split = coins % 8
result = 0

while split < 8:
    if split != 0:
        result = coins - split
        coins = result // 8

    else:
        coins = coins // 8

print(coins)