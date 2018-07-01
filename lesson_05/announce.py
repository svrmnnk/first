quantity = int(input("type the number of parts in announcement: "))

announcement = []

for i in range(quantity):
    announcement.append(input("type the line of announcement: "))

number_announcement = int(input("number of lines to announce: "))
numbers = []
for i in range(number_announcement):
    line_number = int(input("choose your lines: "))
    if line_number not in range(quantity):
        print("your announcement is cancelled")
    else:
        numbers.append(line_number)

for index in numbers:
    print(announcement[index-1])

