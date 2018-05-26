number = int(input("number: "))
k = 0
result = ""
for i in range(1, number + 1):
    if number % i == 0:
        result += str(i)
        k += 1
        if i != number:
            result += " "
print(result)
if k < 3:
    print("ПРОСТОЕ")
else:
    print("NIET")
