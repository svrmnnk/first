import random

n = 4
m = 5

grid = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(-10,5))
    grid.append(row)

for row in grid:
    for element in row:
        print(element, end = " ")
    print()

average = 1
sum = 0.0
for i in range(n):
    for j in range(m):
        sum = sum + grid[i][j]
    average = sum / m
    for j in range(m):
        if grid[i][j] < 0:
            grid[i][j] = average
    sum = 0

print()
for row in grid:
    for element in row:
        print(element, end = " ")
    print()