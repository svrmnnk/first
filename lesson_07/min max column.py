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

minimum = 100

for j in range(m):
    maximum = grid[0][j]
    for i in range(n):
        if grid[i][j] > maximum:
            maximum = grid[i][j]
    print(maximum)
    if maximum < minimum:
        minimum = maximum
print()
print(minimum)