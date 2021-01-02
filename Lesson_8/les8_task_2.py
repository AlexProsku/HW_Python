"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class ZeroValue(Exception):
    pass


class IncorrectValue(Exception):
    pass


def my_input():
    try:
        a, b = input("Введите делимое и делитель через пробел: ").split()
        a, b = float(a), float(b)
        if b == 0:
            raise ZeroValue     # вызываем своё исключение
    except ValueError:
        raise IncorrectValue    # подменяем на своё исключение
    return a, b


try:
    c, d = my_input()
    x = c / d
    print(f"{c} / {d} = {x}")
except ZeroValue:
    print("Нельзя делить на 0 !")
except IncorrectValue:
    print("Вы ввели некорректные данные!")
