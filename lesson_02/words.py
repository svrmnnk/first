new_word = input("введите слово: ")

maxWord = new_word
minWord = new_word

while new_word != "стоп":
    if len(new_word) < len(minWord):
        minWord = new_word
    if len(new_word) > len(maxWord):
        maxWord = new_word
    new_word = input("введите еще слово: ")

i = 0
flag = 1
while i < len(minWord):
    if minWord[i] not in maxWord:
        flag = 0
        print("НЕТ")
        break
    i = i + 1

if flag == 1:
    print("ДА")

print(minWord)
print(maxWord)
