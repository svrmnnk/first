t = float(input("insert temperature: "))

while t > 0 :
    if 15.5 < t < 28:
        print("НОРМАЛЬНО")
    elif t > 28:
        print("ЖАРКО")
    else:
        print("ХОЛОДНО")
    break
