number = int(input("type the number: "))
line_count = 1

for i in range(number):
    for j in range(number - 1 - i):
        print(end=" ")
    for j in range(i * 2 + 1):
        print(end="*")
    print()
