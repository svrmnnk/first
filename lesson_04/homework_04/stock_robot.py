price = int(input("type the stock price: "))
new_price = 0
buy = 0
sell = 0
is_sell = False
is_buy = False
while price != 0:
    new_price = price
    price = int(input("type the stock price: "))
    if new_price < price and is_buy == False:
        buy = price
        is_buy = True
    elif new_price > price and is_sell == False:
        sell = price
        is_sell = True

print(buy, sell, sell - buy)
