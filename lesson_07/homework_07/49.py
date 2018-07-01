n = 7
m = 7

grid = [[0]* m for i in range(n)]
print(grid)

first_line = 0
k = 1

for j in range(m):
    grid[first_line][j] = k
    k += 1

last_column = 6
for i in range(1, n):
    grid[i][last_column] = k
    k += 1

last_line = 6
for j in range(5,-1, -1):
    grid[last_line][j] = k
    k += 1

first_column = 0
for i in range(n-2,0, -1):
    grid[i][first_column] = k
    k += 1

second_line = 1
for j in range(1, m-1, 1):
    grid[second_line][j] = k
    k += 1

sixth_column = 5
for i in range(2, n-1):
    grid[i][sixth_column] = k
    k += 1

sixth_line = 5
for j in range(4,0, -1):
    grid[sixth_line][j] = k
    k += 1

second_column = 1
for i in range(n-3,1, -1):
    grid[i][second_column] = k
    k += 1

third_line = 2
for j in range(m-5,m-2):
    grid[third_line][j] = k
    k += 1

fifth_column = 4
for i in range(n-4, n-2):
    grid[i][fifth_column] = k
    k += 1

fifth_line = 4
for j in range(m-4,m-6, -1):
    grid[fifth_line][j] = k
    k += 1

fourth_line = 3
for j in range(m-5,m-3):
    grid[fourth_line][j] = k
    k += 1

for row in grid:
    print()
    for element in row:
        print(element, end = " ")
    print()