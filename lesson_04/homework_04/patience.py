patience = int(input("how patient are you: "))

count = 0
errors = 0

while patience != 0:
    pupil = input("type the count: ")
    if pupil != "one":
        print("Правильных отсчетов было: ", count, ", но теперь вы ошиблись.")
        count = 0
        errors = errors + 1
        patience = patience - 1

        if patience == 0:
            break
        continue
    count += 1
    pupil = input("type the count: ")
    if pupil != "two":
        print("Правильных отсчетов было: ", count, ", но теперь вы ошиблись.")
        count = 0
        errors = errors + 1
        patience = patience - 1

        if patience == 0:
            break
        continue
    count += 1
    pupil = input("type the count: ")
    if pupil != "three":
        print("Правильных отсчетов было: ", count, ", но теперь вы ошиблись.")
        count = 0
        errors = errors + 1
        patience = patience - 1
        if patience == 0:
            break
        continue
    count += 1
    pupil = input("type the count: ")
    if pupil != "four":
        print("Правильных отсчетов было: ", count, ", но теперь вы ошиблись.")
        count = 0
        errors = errors + 1
        patience = patience - 1

        if patience == 0:
            break
        continue
    count += 1

if patience == 0:
    print("На сегодня хватит")