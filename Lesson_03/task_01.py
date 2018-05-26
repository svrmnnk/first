temp = float(input("temperature: "))
day = 0

while temp < 22.0:
    temp = float(input("temperature: "))
    day += 1

result = day // 7
print(result)