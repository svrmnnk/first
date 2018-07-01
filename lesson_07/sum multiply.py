import random

n = 4
m = 5

k = 2

grid = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(1,20))
    grid.append(row)

for row in grid:
    for element in row:
        print(element, end = " ")
    print()

sum = 0
multiply = 1

for i in range(n):
    sum += grid[i][k-1]
    multiply = multiply * grid[i][k-1]

print(sum)
print(multiply)