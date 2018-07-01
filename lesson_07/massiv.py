import math

n = 3

grid = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input("type the number: ")))
    grid.append(row)

print(grid)

sumTotal = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] < 0 and grid[i][j] % 2 !=0:
            sumTotal += math.fabs(grid[i][j])
print(sumTotal)