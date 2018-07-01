login = input("type your name: ")
is_ok = True
for l in login:
    if not ((ord('A') <= ord(l) <= ord('Z'))
            or (ord('a') <= ord(l) <= ord('z')) or (ord('0') <= ord(l) <= ord('9')) or (l == "_")):
        print('Wrong symbol: ',l)
        is_ok = False
        break

if is_ok == True:
    print("OK")

