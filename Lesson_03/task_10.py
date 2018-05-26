number = int(input("number: "))

for i in range(1, number + 1):
    for j in range(1, number + 1):
       print(i * j,end = "\t")
    print()