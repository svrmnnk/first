number_row = int(input("type the number of rows: "))


cat_find = False

for i in range(number_row):
    phrase = input("type the phrase: ")
    if "cat" in phrase or "Cat" in phrase:
        cat_find = True

    elif "dog" in phrase or "Dog" in phrase:
        cat_find = False

if cat_find == True:
    print("MEOW")
else:
    print("NOPE")