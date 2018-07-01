lines = int(input("type the number of lines: "))
columns = int(input("type the number of columns: "))

total = lines * columns

list = []

for i in range(total):
    list.append(input("type your word: "))

for index in range(columns):
    print(list[index], end = " ")