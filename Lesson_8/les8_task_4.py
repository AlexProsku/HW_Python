"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""


class WareHouse:
    def __init__(self):
        pass


class OfficeEquipment:
    def __init__(self, type_eq, model, manufacture, interfaces):
        self.model = model
        self.type_eq = type_eq
        self.manufacture = manufacture
        self.interfaces = interfaces


class Printer(OfficeEquipment):
    def __init__(self, color_printing, print_speed, print_format, print3d, type_eq, model, manufacture, interfaces):
        super().__init__(type_eq, model, manufacture, interfaces)
        self.color_printing = color_printing
        self.print_speed = print_speed
        self.print_format = print_format
        self.print3d = print3d


class Scanner(OfficeEquipment):
    def __init__(self, scan_speed, scan_format, type_eq, model, manufacture, interfaces):
        super().__init__(type_eq, model, manufacture, interfaces)
        self.scan_speed = scan_speed
        self.scan_format = scan_format


class Copier(OfficeEquipment):
    def __init__(self, scan_speed, print_speed, speed_copy, paper_format, type_eq, model, manufacture,
                 interfaces=None):
        super().__init__(type_eq, model, manufacture, interfaces)
        self.scan_speed = scan_speed
        self.print_speed = print_speed
        self.speed_copy = speed_copy
        self.paper_format = paper_format
