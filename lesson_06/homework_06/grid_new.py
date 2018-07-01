n = int(input("type the number: "))

#grid = [[0]*n]* n

grid = []

# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(0)
#     grid.append(row)

grid = [[0] * n for i in range(n)]

for row in grid:
    for element in row:
        print(element, end = " ")
    print()

j = 0
for i in range(len(grid)-1,-1,-1):
        grid[i][j] = 1
        j+=1

for row in grid:
    for element in row:
        print(element, end = " ")
    print()

k = 0
for i in range(len(grid)-1, -1, -1):
    for j in range(1 + k, len(grid)):
        grid[i][j] = 2
    k += 1

for row in grid:
    for element in row:
        print(element, end = " ")
    print()