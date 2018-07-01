word = input("type the word: ")
first_time = -1
total_raw = 0
is_find_cat = False
k = 1
while word != "STOP":
    if "cat" in word:
        total_raw += 1
        if is_find_cat == False:
            first_time = k
            is_find_cat = True

    word = input("type the word: ")
    k += 1
print(total_raw, first_time)