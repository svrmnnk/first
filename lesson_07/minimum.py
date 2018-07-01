import random
n = 5

grid = [[random.randint(0,100)] * n for i in range(n)]

print(grid)

j = 0
minimum = grid[0][n-1]
for i in range(len(grid)-1,-1,-1):
        if grid[i][j] < minimum:
            minimum = grid[i][j]
        j+=1
print(minimum)