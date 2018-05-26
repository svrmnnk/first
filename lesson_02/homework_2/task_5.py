pass1 = input("create your password: ")
pass2 = input("retype your password: ")

while len(pass1) > 7:
    if pass1 != pass2:
        print("Различаются!")

    else:
        print("OK")
    break

else:
    print("Короткий!")