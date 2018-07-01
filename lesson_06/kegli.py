kegli_quantity = int(input("type the number of kegli: "))

kegli_view = ['I'] * kegli_quantity

shots_number = int(input("type the number of shots to make: "))

for i in range(shots_number):
    left = int(input("keglya sbitaya sleva: "))
    right = int(input("keglya sbitaya sprava: "))
    for j in range(left-1, right):
        kegli_view[j] = "."

#print(kegli_view)
print(''.join(kegli_view))