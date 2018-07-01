lines = int(input("type the number of lines: "))

list = []

for i in range(lines):
    list.append(input("type your line: "))

letter = int(input("type the number of letter to use: "))

for word in list:
    if letter < len(list):
        print(word[letter-1])