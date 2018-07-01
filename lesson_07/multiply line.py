import random

n = 3
m = 4

k = 1

grid = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(1,9))
    grid.append(row)

for row in grid:
    for element in row:
        print(element, end = " ")
    print()

multiply = 1

for j in range(m):
    for i in range(n):
        multiply = multiply * grid[i][j]
    print(multiply)
    multiply = 1