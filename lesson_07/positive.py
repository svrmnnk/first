import random

n = 3
m = 3

grid = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(1,20))
    grid.append(row)

print(grid)

sum = 0
for j in range(m):
    for i in range(n):
        sum+= grid[i][j]
    print(sum/n)
    sum = 0