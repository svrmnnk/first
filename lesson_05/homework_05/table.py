lines = int(input("type the number of lines: "))
columns = int(input("type the number of columns: "))

# list_1 = []
# list_2 = []
# list_3 = []
#
# for x in range(columns):
#     list_1.append(input("type your word: "))
#
# for x in range(columns):
#     list_2.append(input("type your word: "))
#
# for x in range(columns):
#     list_3.append(input("type your word: "))
#
# for x in list_1:
#     for y in list_2:
#         for z in list_3:
#             print(x,y,z)

table = []

for i in range(lines):
    row = []
    for j in range(columns):
        row.append(input("type your word: "))
    table.append(row)
for row in table:
    for element in row:
        print(element, end = " ")
    print()
print(table[2][0])
