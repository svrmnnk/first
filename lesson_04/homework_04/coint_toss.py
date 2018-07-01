coin = input("your coin toss result: ")
count = 0
max_count = 0
for l in coin:
    if l == "o":
        count += 1
    elif count > max_count:
        max_count = count
        count = 0
if count > max_count:
    max_count = count
print(max_count)