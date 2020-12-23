"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    # def check_data(self):         # Можно использовать для отладки переданных значений переменных
    #     data_incorrect = []
    #     for el in self.name, self.surname, self.position:
    #         if type(el) is not str:
    #             data_incorrect.append(el)
    #     for el in self._income.values():
    #         if type(el) is int or type(el) is float:
    #             pass
    #         else:
    #             data_incorrect.append(el)
    #     if data_incorrect == []:
    #         print("Атрибуты заполнены с корректным типом данных")
    #     else:
    #         print(f"Следующие введённые значения некорректны: {', '.join(data_incorrect)}")


class Position(Worker):
    def get_full_name(self):
        full_name = self.name + " " + self.surname
        return full_name

    def get_total_income(self):
        income = self._income.get("wage") + self._income.get("bonus")
        return income


P1 = Position("Иван", "Петров", "оператор", 30000, 2000.5)
P2 = Position("Степан", "Сидоров", "начальник", 65000, 8000)
P3 = Position("Петр", "Игнатьев", "специалист", 40000, 3000)
for el in P1, P2, P3:
    print(f"Сотрудник {el.get_full_name()} имеет доход (с учётом премии) {el.get_total_income()}")
# P1.check_data()       # Можно использовать для отладки переданных значений переменных
