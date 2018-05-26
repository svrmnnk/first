coins = int(input("Количество монет у Учителя: "))

while coins > 0:
        result = coins % 8
       # print("ost=",result)
        coins = coins // 8
       # print("main=",coins)
print(result)
