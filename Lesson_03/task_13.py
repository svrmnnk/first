people = int(input("number of people: "))
sum = 0
q = 0

for i in range(0, people):
    iq = int(input("iq level: "))
    sum += iq
    q += 1
    if sum / q  == iq:
        print(0)
    elif sum / q < iq:
        print(">")
    else:
        print("<")
