n = int(input("type the number of things to buy: "))

shopping = []

for i in range(n):
    shopping.append(input("type what you need to buy: "))

for x in shopping:
    print(x)