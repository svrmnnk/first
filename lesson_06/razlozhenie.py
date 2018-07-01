n = int(input("type your number: "))

base = 10
a = 1

remainder = []
num = []

#1 / 15   100    0,0606
while not (a in remainder):
    remainder.append(a)
    a = a * base
    num.append(a//n)
    a = a % n
print(num)
print(remainder)
print(a)
period = False
for i in range(len(remainder)):
    if remainder[i] == a:
        period = True
    if period:
        print(num[i], end = "")