t1 = input("your city: ")
t2 = input("second city: ")

while len(t1) > 0 and len(t2) > 0:
    if t1[-1] == t2[0]:
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")
    break