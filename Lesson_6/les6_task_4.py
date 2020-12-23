"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):               # сообщает, что машина поехала
        if self.speed > 0:
            return f"Машина поехала (едет) со скоростью {self.speed}!"
        else:
            return f"Машина не едет"

    def stop(self):             # сообщает, что машина остановилась
        if self.speed == 0:
            return f"Машина остановилась (стоит)!"
        else:
            return f"Машина в движении"

    def turn(self, direction="прямо"):  # сообщает, что машина повернула
        if self.speed == 0:
            return f"Мажина не может повернуть без движения (без скорости)"
        elif direction == "прямо" and self.speed > 0:
            return f"Машина едет прямо"
        else:
            return f"Машина повернула {direction}"

    def show_speed(self):       # показывает текущую скорость автомобиля
        return self.speed


class TownCar(Car):
    def show_speed(self):    # показывает текущую скорость автомобиля
        if self.speed > 60:
            return f"Вы превысили скорость!"
        else:
            return self.speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):    # показывает текущую скорость автомобиля
        if self.speed > 40:
            return f"Вы превысили скорость!"
        else:
            return self.speed


class PoliceCar(Car):
    pass


TC = TownCar(70, "белый", "А521ВВ99", False)
SP = SportCar(100, "чёрный", "Г881ВВ99", False)
WC = WorkCar(50, "серый", "Р331ВВ99", False)
PC = PoliceCar(0, "бело-синий", "П222ПП77", True)

for i, el in enumerate((TC, SP, WC, PC), 1):
    print(f"Параметры авто({i}): скорость = {el.speed}, цвет - {el.color}, имя (номер) - {el.name}, "
          f"признак полиции - {el.is_police}")
    print(f"Ваша скорость: {el.show_speed()}")
    print(el.go())
    print(el.stop())
    print(f"{el.turn('направо')}\n")
