import random

n = 4
m = 5

k = 1

grid = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(1,100))
    grid.append(row)

for row in grid:
    for element in row:
        print(element, end = " ")
    print()

sum = 0

for i in range(n):
    for j in range(m):
        sum += grid[i][j]
    print(sum)
    sum = 0
