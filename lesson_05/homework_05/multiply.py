numbers = int(input("how many numbers: "))

values = []

for i in range(numbers):
    values.append(int(input("type the number: ")))

result = int(input("type the potential multiply result: "))

count = False

for i in range(len(values)):
    for j in range(i+1, len(values)):
        print(values[i], values[j])
        if result == values[i]*values[j]:
            count = True
        else:
            count = False

if count == True:
    print("YES")
else:
    print("NO")