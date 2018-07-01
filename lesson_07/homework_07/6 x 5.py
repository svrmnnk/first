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

# for j in range(m):
#     for i in range(n-1):
#             temp2 = grid[i][j]
#             grid[i][j] = grid[i+1][j]
#             grid[i+1][j] = temp2

for i in range(n):
    for j in range(0,m-1, 2):
       grid[i][j], grid[i][j+1] = grid[i][j+1], grid[i][j]

print()
for row in grid:
    for element in row:
        print(element, end = " ")
    print()

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