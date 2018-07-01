import random

n = 18 # number of employees
m = 12 # 12 months of the year with salary data

k = 5

grid = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(1,3)) #salary ranging from 1 to 3 k
    grid.append(row)

for row in grid:
    for element in row:
        print(element, end = " ")
    print()

sum = 0

for i in range(n):
    sum += grid[i][k]

print("Total salary paid in june: ", sum)