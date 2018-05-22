total = 0
price = float(input("Введите цену: "))
while price > 0:
    if price > 1000:
        price *= 0.95
    total = total + price
    price = float(input("Введите цену: "))
print(total)