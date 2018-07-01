number = int(input("number of raws: "))
is_find = False

for i in range(number):
    word = input(" type the word: ")
    if "кот" in word or "Кот" in word:
        is_find = True
        break

if is_find == True:
    print("МЯУ")
else:
    print("НЕТ")