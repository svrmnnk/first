currency = input("Hello, type your currency: ")

while currency != "":
    if currency == "Roubles":
        print("Choose your operation.")
    else:
        print("Unfortunately, ", currency, "are not available for operations, please choose another currency.")
    currency = input("Hello, type your currency: ")

print("Good bye")