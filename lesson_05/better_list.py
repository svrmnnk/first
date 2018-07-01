general = int(input("number of items to buy: "))

to_buy_items = []
to_buy_quantity = []

for i in range(general):
    to_buy_items.append(input("type what you need to buy: "))
    to_buy_quantity.append(int(input("type the quantity of the previous item: ")))

for x in range(len(to_buy_items) - 1,-1, -1):
    print(to_buy_items[x], to_buy_quantity[x])