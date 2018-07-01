import random

n = 4
m = 4

k1 = 1
k2 = 3

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

new_grid = []

for j in range(m):
    temp = grid[k1][j]
    grid[k1][j] = grid[k2][j]
    grid[k2][j] = temp

print ()
for row in grid:
    for element in row:
        print(element, end = " ")
    print()