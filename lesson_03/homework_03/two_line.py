word1 = input("type first word: ")
word2 = input("type second word: ")
count = 0

for letter in word1:
    if letter in word2:
        count += 1

print(count)

count2 = 0

for i in range(len(word1)):
        if word1[i] == word2[i]:
            count2 += 1

print(count2)