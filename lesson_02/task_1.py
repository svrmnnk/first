max_length = len('Константин Константинович Константинопольский')
name = input()
print('Здравствуйте,', name)
second_name = input()
surname = input()
full_name = name + ' ' + second_name + ' ' + surname
full_name_length = len(name) + len(second_name) + len(surname) + 2
if len(full_name) != full_name_length:
    print('Ошибка: что-то пошло не так.')
else:
    if len(full_name) > max_length:
        print('Извините, ваше имя слишком длинное. Попробуйте изменить имя.')
        name = input()
#       surname = input()
    print(len(name), len(full_name))
print('Спасибо, что воспользовались нашей программой!')