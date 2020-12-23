"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title  # название

    def draw(self):         # отрисовка
        return f"Запуск отрисовки"


class Pen(Stationery):      # ручка
    def draw(self):
        return f"Запуск отрисовки ручкой"


class Pencil(Stationery):   # карандаш
    def draw(self):
        return f"Запуск отрисовки карандашом"


class Handle(Stationery):   # маркер
    def draw(self):
        return f"Запуск отрисовки маркером"


Stat = Stationery("КанцТовары")
S_Pen = Pen("Ручка")
S_Pencil = Pencil("Карандаш")
S_Handle = Handle("Маркер")

for el in Stat, S_Pen, S_Pencil, S_Handle:
    print(el.draw())
