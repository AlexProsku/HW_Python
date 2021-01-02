"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение
должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""


class NoDigit(Exception):
    pass


def check_digit(item_for_check):
    if item_for_check.isdigit():
        return item_for_check
    else:
        raise NoDigit


my_list = []
while True:
    item = input("Введите число (для выхода - введите stop или нажмите Enter): ")
    try:
        if item == "stop" or item == "":
            break
        else:
            my_list.append(check_digit(item))
    except NoDigit:
        print("Вы ввели не число!")
        continue
print(f"Введённый список числе: {my_list}")
