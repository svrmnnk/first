phrase = input("Что с вами? ")
count = 1

while "Спасибо." not in phrase:
    phrase = input("Что с вами? ")
    count += 1

print(count)