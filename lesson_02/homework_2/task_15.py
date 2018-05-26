word1 = input("type your word: ")
word2 = input("type your word: ")

while word1[-1] == "ь":
    if word1[-2] == word2[0]:
        print("ВЕРНО")
    word1 = input("type your word: ")

else:
    if word1[-1] == word2[0]:
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")