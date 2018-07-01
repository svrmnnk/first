count = 0
sum = 0
c = 0
stop_number = 0
number = int(input("type the number: "))

flag = False
while number != stop_number:
    sum = sum + number
    count += 1
    if sum == 10:
        c = count
    number = int(input("type the number: "))

print(c)