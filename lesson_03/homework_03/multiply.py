column = int(input("type the number of columns: "))
raw = int(input("type the number of raws: "))

for i in range(1, raw+1):
    for j in range (1 ,column+1):
        print(j/i, end = " ")

    print()