"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle


def iter_int(start_numb, stop_numb):
    iter_list = []
    iter_count = count(start_numb)
    for i in iter_count:
        iter_list.append(i)
        if i >= stop_numb:
            break
    return iter_list


def cycle_list(my_list, quant):
    new_list = []
    iter_cycle = cycle(my_list)
    for i in iter_cycle:
        new_list.append(i)
        if len(new_list) >= len(my_list) * quant:
            break
    return new_list


list_b = [300, 2, 12, 44]
print(iter_int(5, 54))
print(cycle_list(list_b, 3))
