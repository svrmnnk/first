a = int(input("type your number: "))
b = int(input("type your number: "))
c = str(input("type your action: "))

if c == "-":
    print(a-b)
elif c == "+":
    print(a+b)
elif c == "*":
    print(a*b)
elif c == "/" and b == 0:
    print("88888")
elif c == "/":
    print(a/b)

else:
    print("88888")