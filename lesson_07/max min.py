import random

n = 7
m = 6

k = 1

grid = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(10,99))
    grid.append(row)

for row in grid:
    for element in row:
        print(element, end = " ")
    print()


maximum = 0

for i in range(n):
    minimum = grid[i][0]
    for j in range(m):
        if grid[i][j] < minimum:
            minimum = grid[i][j]
    print(minimum)
    if minimum > maximum:
        maximum = minimum
print(maximum)