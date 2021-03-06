"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""


class TrafficLight:
    def __init__(self):
        self.__color = ['красный', 'жёлтый', 'зелёный']
        self.__time_change = {'красный': 7, 'жёлтый': 2, 'зелёный': 10}
        self.__time_working = 0

    def running(self, duration=50):
        from time import sleep
        from itertools import cycle
        for el in cycle(self.__color):
            if self.__color != ['красный', 'жёлтый', 'зелёный']:
                print("Хакеры х..ы, вы поломали светофор!")
                break
            if self.__time_working > duration:
                print("Работа светофора завершена!")
                break
            print(f"Загорелся {el}")
            time_change = self.__time_change.get(el)
            self.__time_working += time_change
            sleep(time_change)


TL1 = TrafficLight()
TL1.running(30)
