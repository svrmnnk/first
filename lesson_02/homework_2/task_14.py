word = input("word starting with a: ")

while "а" in word or "А" in word:
    print("ДА")
    break
else:
    print("НЕТ")