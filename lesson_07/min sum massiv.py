import random

n = 5
m = 7

grid = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(0,15))
    grid.append(row)

for row in grid:
    for element in row:
        print(element, end = " ")
    print()

sum = 0
minimum = 16
index = - 1
for j in range(m):
    for i in range(n):
        sum = sum + grid[i][j]
    for i in range(n):
        if grid[i][j] < minimum:
            minimum = grid[i][j]
            index = i
    grid[index][j] = sum
    sum = 0
    minimum = 16

print()
for row in grid:
    for element in row:
        print(element, end = " ")
    print()

