word1 = input("type your word: ")
word2 = input("type your word: ")

while word1[-1] == word2[0]:
    word1 = input("type your word: ")
    word1, word2 = word2, word1

