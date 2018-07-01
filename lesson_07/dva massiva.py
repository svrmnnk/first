import random

n = 5
m = 7

grid = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(2,9))
    grid.append(row)

for row in grid:
    for element in row:
        print(element, end = " ")
    print()

min_sum = 80
sum = 0
for j in range(m):
    for i in range(n):
        if grid[i][j] % 2 == 0:
            sum = sum + grid[i][j]
    if sum < min_sum:
        min_sum = sum
    sum = 0

print(min_sum)

grid_2 = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        grid_2[i][j] = grid[i][j] - min_sum

for row in grid_2:
    for element in row:
        print(element, end = " ")
    print()
