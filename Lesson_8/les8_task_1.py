"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
from datetime import date


class Date:
    def __init__(self):
        pass

    @classmethod
    def extract(cls, date_in):
        return int(date_in[:2]), int(date_in[3:5]), int(date_in[6:])

    @staticmethod
    def validation(date_in):
        try:
            if date(int(date_in[6:]), int(date_in[3:5]), int(date_in[:2])):
                return f"Дата корректная"
        except ValueError:
            return f"Дата некорректная"


print(Date.extract("01-02-2020"))
print(f"Дата 30-03-2020 - {Date.validation('30-03-2020')}")
print(f"Дата 30-02-2020 - {Date.validation('30-02-2020')}")
