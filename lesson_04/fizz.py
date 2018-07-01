number1 = int(input("type first number: "))
number2 = int(input("type second number: "))

for i in range(number1, number2+1):

    if i % 3 == 0:
        print("Fizz", end="")
    if i % 5 == 0:
        print("Buzz")
    print()


