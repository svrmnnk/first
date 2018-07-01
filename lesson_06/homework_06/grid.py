n = int(input("type your number: "))

list = []

zeroes = [0]
ones = [1]
twos = [2]
#нужно сделать так, чтобы в список list добавлялось соответствующее количество списков с числами таким образом
# чтобы, например, при введении числа 3, получился list = [[0,0,1],[0,1,2],[1,2,2]]
for i in range(n):
    list.append((zeroes * (n-1)) + ones)
    list.append((zeroes * (n-2)) + ones + (twos * (n-2)))
    list.append((ones + (twos * (n-1))))

print(list)
