"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
"""


class NotEnough(Exception):
    pass


class NoProduct(Exception):
    pass


class WareHouse:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.dict_eq = {}

    def add_to_wh(self, equipment, quantity):
        if self.dict_eq.get(equipment.type_equipment):
            self.dict_eq.update({equipment.type_equipment: self.dict_eq.get(equipment.type_equipment) + quantity})
        else:
            self.dict_eq.setdefault(equipment.type_equipment, quantity)

    def extract_wh(self, equipment, quantity):
        try:
            if self.dict_eq.get(equipment.type_equipment) == quantity:
                self.dict_eq.pop(equipment.type_equipment)
            elif self.dict_eq.get(equipment.type_equipment) > quantity:
                self.dict_eq.update({equipment.type_equipment: self.dict_eq.get(equipment.type_equipment) - quantity})
            else:
                raise NotEnough
        except TypeError:
            raise NoProduct

    def __str__(self):
        return f"Склад {self.name} {self.address} с товаром:\n{self.dict_eq}"


class OfficeEquipment:
    def __init__(self, model, manufacture, interfaces):
        self.model = model
        self.manufacture = manufacture
        self.interfaces = interfaces
        self.type_eq = self.__class__.__name__

    @property
    def type_equipment(self):
        return f"{self.type_eq} {self.manufacture} {self.model}"

    def __str__(self):
        return f"{self.type_eq} {self.manufacture} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, color_printing, print_speed, print_format, print3d, model, manufacture, interfaces):
        super().__init__(model, manufacture, interfaces)
        self.color_printing = color_printing
        self.print_speed = print_speed
        self.print_format = print_format
        self.print3d = print3d


class Scanner(OfficeEquipment):
    def __init__(self, scan_format, model, manufacture, interfaces):
        super().__init__(model, manufacture, interfaces)
        self.scan_format = scan_format


class Copier(OfficeEquipment):
    def __init__(self, speed_copy, paper_format, model, manufacture,
                 interfaces):
        super().__init__(model, manufacture, interfaces)
        self.speed_copy = speed_copy
        self.paper_format = paper_format


print1 = Printer("monochrome", 11, "A4", False, "Z5120", "HP", interfaces=["USB", "Ethernet"])
print2 = Printer("color", 15, "A4", False, "A15", "HP", ["USB"])
print3 = Printer("color", 2, "A4", True, "WG343", "PROFI", ["USB"])
scanner1 = Scanner("A3", "AZ342", "Samsung", ["USB"])
scanner2 = Scanner("A4", "AZ452", "Epson", ["USB"])
copier1 = Copier(5, "A4", "VX343", "Xerox", ["USB", "WiFi"])
copier2 = Copier(3, "A3", "A453", "Xerox", ["USB", "Ethernet" "WiFi"])

wh1 = WareHouse("Dom1", "Moscow, Domodedovo, 2")
wh2 = WareHouse("Pol", "Moscow, Polyanka, 43")

wh1.add_to_wh(print1, 2)
wh1.add_to_wh(print1, 7)
wh1.add_to_wh(print2, 4)
wh1.add_to_wh(scanner2, 5)
wh1.add_to_wh(copier1, 4)
print(f"{wh1}\n{wh2}\n")

try:
    wh1.extract_wh(print1, 11)
    wh2.add_to_wh(print1, 11)
except NotEnough:
    print("Невозможно переместить товар, т.к. недостаточное количество\n")

wh1.extract_wh(print1, 5)
wh2.add_to_wh(print1, 5)
print(f"{wh1}\n{wh2}\n")

wh1.extract_wh(print1, 4)
wh2.add_to_wh(print1, 4)
print(f"{wh1}\n{wh2}\n")

try:
    wh1.extract_wh(print1, 4)
    wh2.add_to_wh(print1, 4)
except NotEnough:
    print("Невозможно переместить товар, т.к. недостаточное количество\n")
except NoProduct:
    print("Невозможно переместить товар, т.к. данного товара совсем нет на складе или он не заведён\n")
print(f"{wh1}\n{wh2}\n")
