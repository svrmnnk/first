import random

n = 6
m = 8

grid = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(-5,15))
    grid.append(row)

for row in grid:
    for element in row:
        print(element, end = " ")
    print()

min_sum_line_index = 0
max_sum_line_index = 0

min_sum = 1000
max_sum = -1000

sum = 0

for i in range(n):
    for j in range(m):
        sum = sum + grid[i][j]
    if sum < min_sum:
        min_sum = sum
        min_sum_line_index = i
    if sum > max_sum:
        max_sum = sum
        max_sum_line_index = i
    sum = 0

print(min_sum)
print(max_sum)

print(min_sum_line_index)
print(max_sum_line_index)

k1 = max_sum_line_index
k2 = min_sum_line_index

for j in range(m):
    temp = grid[k1][j]
    grid[k1][j] = grid[k2][j]
    grid[k2][j] = temp

print ()
for row in grid:
    for element in row:
        print(element, end = " ")
    print()