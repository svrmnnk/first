lines = int(input("type the number of lines: "))

database = []

for i in range(lines):
    database.append(input("type your line: "))

keyword = input("type what to search: ")
for x in range(lines):
    if keyword in database[x]:
        print(database[x])