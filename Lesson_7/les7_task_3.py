"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, cells_num):
        self.cells_num = int(cells_num)

    def __add__(self, other):
        return self.cells_num + other.cells_num

    def __sub__(self, other):
        if self.cells_num > other.cells_num:
            return self.cells_num - other.cells_num
        else:
            return 0        # некий плохой хардкод

    def __mul__(self, other):
        return self.cells_num * other.cells_num

    def __truediv__(self, other):
        return round(self.cells_num / other.cells_num)

    def make_order(self, row_num):
        order = ""
        for i in range(self.cells_num // row_num):
            order += f"{'*' * row_num}\n"
        order += f"{'*' * (self.cells_num % row_num)}"
        if order == "":
            return f"Невозможно произвести действие с клеткой"
        else:
            return order


a, b = Cell(15), Cell(7)          # для позитивного сценария
# a, b = Cell(7), Cell(15)        # для негативного сценария с вычитанием и делением
add_cell = Cell(a + b)
sub_cell = Cell(a - b)
mul_cell = Cell(a * b)
div_cell = Cell(a / b)
print(f"Клетка а:\n{a.make_order(5)}\n" + f"Клетка b:\n{b.make_order(5)}")
print(f"Сложиение клеток а и b:\n{add_cell.make_order(5)}\n" +
      f"Вычитание клеток а и b:\n{sub_cell.make_order(5)}\n" +
      f"Умножение клеток а и b:\n{mul_cell.make_order(5)}\n" +
      f"Деление клеток а и b:\n{div_cell.make_order(5)}")
