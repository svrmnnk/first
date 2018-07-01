import random

n = 5 # 5 years
m = 8 # 8 groups on every year

grid = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(5,15)) #number of students in one group from 5 to 15
    grid.append(row)

for row in grid:
    for element in row:
        print(element, end = " ")
    print()

k = random.randint(0,4)
print("We are calculating the number of students on the year: ", k+1)

sum = 0

for j in range(m):
    sum += grid[k][j]

print("The number of students on the year ", k+1, "is: ", sum)