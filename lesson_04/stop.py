num_str = -1
forbidden_word = "STOP"
count = 1
word = input("type the word: ")
is_find = False
while word != forbidden_word:
    if ("cat" in word or "Cat" in word) and is_find == False:
        num_str = count
        is_find = True
    count += 1
    word = input("type the word: ")
print(num_str)

