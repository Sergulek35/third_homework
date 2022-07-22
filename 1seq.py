# МОДУЛЬ 1"
"""Пользователь вводит количество элементов будущего списка
После этого по очереди по одной вводит любые цифры
Сохранить цифры в список
Отсортировать список по возрастанию и вывести на экран"""

amount_numbers = ''
while not amount_numbers.isdigit():
    amount_numbers = input('Введите количество цифр: ')

amount_numbers = int(amount_numbers)

user_digits = []
number_digits = 1

for i in range(amount_numbers):
    numbers = ''
    while not numbers.isdigit():
        print('Введите число:', number_digits)
        numbers = input()
    numbers = int(numbers)
    number_digits += 1
    user_digits.append(numbers)

user_digits.sort()
print('-' * 50)
print(user_digits)
