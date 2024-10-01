# Работа со словарями
my_dict = {'Efim': 1992, 'Marina': 2001, 'Kirill': 2004}
print(my_dict)
print(my_dict.get('Efim'))
print(my_dict.get('Anton', 'Такого ключа нет'))
print(my_dict.pop('Marina'))
my_dict.update({'Maxim': 1999, 'Sasha': 1991})
print(my_dict)
# Работа с множествами
my_set = {1, 2, 1, 1, 2, 42.314, 'apple', 42.314}
print(my_set)
print(my_set.add(5))
print(my_set)
print(my_set.remove(1))
print(my_set)
