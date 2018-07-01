n = 10
m = 10

grid = [[0]* m for i in range(n)]
print(grid)

k = 1

first_column = 0
for i in range(0,10):
    grid[i][first_column] = k
    k += 1

second_column = 1
for i in range(9,-1,-1):
    grid[i][second_column] = k
    k += 1

third_column = 2
for i in range(0,10):
    grid[i][third_column] = k
    k += 1

fourth_column = 3
for i in range(9,-1,-1):
    grid[i][fourth_column] = k
    k += 1

fifth_column = 4
for i in range(0,10):
    grid[i][fifth_column] = k
    k += 1

sixth_column = 5
for i in range(9,-1,-1):
    grid[i][sixth_column] = k
    k += 1

seventh_column = 6
for i in range(0,10):
    grid[i][seventh_column] = k
    k += 1

eigth_column = 7
for i in range(9,-1,-1):
    grid[i][eigth_column] = k
    k += 1

ninth_column = 8
for i in range(0,10):
    grid[i][ninth_column] = k
    k += 1

tenth_column = 9
for i in range(9,-1,-1):
    grid[i][tenth_column] = k
    k += 1

for row in grid:
    for element in row:
        print(element, end = " ")
    print()

sum = 0
print()
for j in range(m):
    for i in range(n):
        sum = sum + grid[i][j]
    print(sum)
    sum = 0
