number1 = int(input("type the first number: "))
operand = input("type your operand: ")
permit = True
while operand != "x":
    if operand == "+":
        number2 = int(input("type the second number: "))
        print(number1 + number2)
        permit = False
    elif operand == "-":
        number2 = int(input("type the second number: "))
        print(number1 - number2)
        permit = False
    elif operand == "*":
        number2 = int(input("type the second number: "))
        print(number1 * number2)
        permit = False
    elif operand == "/":
        number2 = int(input("type the second number: "))
        print(number1 / number2)
        permit = False
    elif operand == "%":
        number2 = int(input("type the second number: "))
        print(number1 % number2)
        permit = False
    elif operand == "!":
        b = 1
        for n in range(1, number1+1):
            b = b * n
            permit = False
        print(b)
    number1 = int(input("type the first number: "))
    operand = input("type your operand: ")
print(number1)