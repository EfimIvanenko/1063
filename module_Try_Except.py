def add_everything_up(a, b):
    try:

        return a + b
    except TypeError:

        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))  # Ожидается: "123.456строка"
print(add_everything_up('яблоко', 4215))  # Ожидается: "яблоко4215"
print(add_everything_up(123.456, 7))  # Ожидается: 130.456
