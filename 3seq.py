# МОДУЛЬ 3
# Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран

# с копией не очень понятно, сам бы не догадался, если бы не разбор

first_list = input(' введите элементы 1-го списка через пробел: ').split()

second_list = input(' введите элементы 2-го списка через пробел: ').split()

for elemet in first_list.copy():
    if elemet in second_list:
        first_list.remove(elemet)
print('Результат - ', first_list)
