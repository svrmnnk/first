word = input("type the word: ")
count = 0
is_find = False
while word != "STOP":
    if "cat" in word or "Cat" in word:
        count += 1
        print(count)
        is_find = True
        break
    word = input("type the word: ")
    count = count + 1

if is_find == False:
    print("-1")

