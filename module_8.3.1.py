class IncorrectVinNumber(Exception):
    """Исключение для некорректного VIN номера."""

    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    """Исключение для некорректных номеров автомобиля."""

    def __init__(self, message):
        self.message = message


class Car:
    """Класс автомобиля с проверкой VIN номера и номеров."""

    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = self.__validate_vin(vin)
        self.__numbers = self.__validate_numbers(numbers)

    def __validate_vin(self, vin_number):
        """Проверяет VIN номер на корректность."""
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return vin_number

    def __validate_numbers(self, numbers):
        """Проверяет номера на корректность."""
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return numbers


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
