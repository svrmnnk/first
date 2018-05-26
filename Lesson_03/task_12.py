falcon = int(input("number of falcons: "))
count = 0

for i in range(0, falcon):
    for j in range(i, -1, -1):
        print("Осталось секунд:", j)
    print("Пуск", i + 1)