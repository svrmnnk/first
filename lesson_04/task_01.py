forbidden_word = 'синхрофазотрон'
# можно было использовать и sep='', чтобы кавычки не отклеились от слова
print('Введите десять слов, но постарайтесь случайно не ввести слово "' + forbidden_word + '"!')
said_forbidden_word = False
for i in range(10):
    if said_forbidden_word:
        print('Напоминаем, будьте осторожнее, не введите снова слово "' + forbidden_word + '"!')
    word = input()
    if word == forbidden_word:
        said_forbidden_word = True
    # вместо предыдущих двух строк также можно написать:
    # said_forbidden_word = (said_forbidden_word or word == forbidden_word)
if said_forbidden_word:
    print('Вы нарушили инструкции.')
else:
    print('Спасибо, что ни разу не упомянули', forbidden_word)