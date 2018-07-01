number_of_items = int(input("type the number of items: "))

items = []
#
for i in range(number_of_items):
    items.append(int(input("type the item: ")))

print(items)

for i in range(1, len(items)):
    print(items[i] + items[i-1])