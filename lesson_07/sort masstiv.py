import random

n = 6
m = 5

grid = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(-5,10))
    grid.append(row)

for row in grid:
    for element in row:
        print(element, end = " ")
    print()

sum = 0
for i in range(n):
    for j in range(m):
        sum = sum + grid[i][j]
print(sum)

for i in range(n):
    for j in range(m-1):
        for k in range(m-1-j):
            if grid[i][k] > grid[i][k+1]:
                temp = grid[i][k]
                grid[i][k] = grid[i][k+1]
                grid[i][k+1] = temp

print()
for row in grid:
    for element in row:
        print(element, end = " ")
    print()

for i in range(n):
    for j in range(m):
        if grid[i][j] < 0:
            grid[i][j] = 0

print()
for row in grid:
    for element in row:
        print(element, end = " ")
    print()

sum_new = 0
for i in range(n):
    for j in range(m):
        sum_new = sum_new + grid[i][j]
print(sum_new)