lines = int(input("type the number of lines: "))
columns = int(input("type the number of columns: "))

table = []

for i in range(lines):
    row = []
    for j in range(columns):
        row.append(input("type your word: "))
    table.append(row)
for row in table:
    for element in row:
        print(element, end=" ")
    print()

table_2 = []
for i in range(columns):
    table_2.append([""] * lines)
print(table_2)

for i in range(len(table)): #по строкам
    for j in range(len(table[0])): #по столбцам
        table_2[j][i] = table[i][j]

for i in range(len(table_2)):
    for j in range(len(table_2[0])):
        print(table_2[i][j], end = " ")
    print()