import random

n = 6
m = 6

grid = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(-10,10))
    grid.append(row)

for row in grid:
    for element in row:
        print(element, end = " ")
    print()

for j in range(m):
    for i in range(n-1):
        for k in range(n-1-i):
            if grid[k][j] > grid[k+1][j]:
                temp = grid[k][j]
                grid[k][j] = grid[k+1][j]
                grid[k+1][j] = temp

print()
for row in grid:
    for element in row:
        print(element, end = " ")
    print()

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            grid[i][j] = 100

print()
for row in grid:
    for element in row:
        print(element, end = " ")
    print()