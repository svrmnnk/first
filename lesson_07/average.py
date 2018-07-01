import random

n = 4
m = 4

k = 1

grid = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(1,9))
    grid.append(row)

for row in grid:
    for element in row:
        print(element, end = " ")
    print()
average_list = []
average = 0
sum = 0
for j in range(m):
    for i in range(n):
      sum += grid[i][j]
    average = sum / n
    sum = 0
    average_list.append(average)
print(average_list)

count = 0
for j in range(m):
    for i in range(n):
        if grid[i][j] > average_list[j]:
            count += 1
    print(count)
    count = 0
