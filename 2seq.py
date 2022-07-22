# МОДУЛЬ 2
"""Пользователь вводит любые цифры через запятую
Сохранить цифры в список
Получить новый список в котором будут только уникальные элементы исходного
Вывести новый список на экран"""

user_number = input('вводите любые цифры через:("," или ";" или "/"): ')
numbers = user_number.replace(';', ' ').replace('/', ' ').replace(',', ' ').split()

unique = []
for number in numbers:
    if numbers.count(number) == 1:
        unique.append(number)

print(unique)
