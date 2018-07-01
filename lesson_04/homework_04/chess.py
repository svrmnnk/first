field = int(input("type the number: "))

row1 = ""
row2 = ""
row3 = ""
row4 = ""
row5 = ""
row6 = ""
row7 = ""
row8 = ""
column = ""

chess = True
# l =  ord('A'), r = ord('H')  for x range(l,l+3)   chr(x)
while field < 9:
    for i in range(field, 0, -1):
        row1 = "A" + str(i)
        print(row1, end = "\t")

    for i in range(field, 0, -1):
        row2 = "B" + str(i)
        print(row2, end = "\t")

    for i in range(field, 0, -1):
        row3 = "C" + str(i)
        print(row3, end = "\t")
        field = 10