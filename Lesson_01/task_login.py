login = input("type your login:")
email = input("type your email:")
is_correct = 0
if "@" in login:
    print("Некорректный у вас логин")
    is_correct = 1
if "@" not in email:
    print("Некорректный у вас емэйл")
    is_correct = 1
if is_correct == 0:
    print("OK")