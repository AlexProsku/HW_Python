# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(a, b):
    try:
        a, b = float(a), float(b)
        result = a / b
    except ZeroDivisionError:
        print("Значение делителя не должно быть нулевым!")
        return
    except ValueError:
        print("Вы ввели не число!")
        return
    if (result % 1) == 0:  # Если в результате целое число, то визуально отсечём у него 0 превращением в int
        result = int(result)
    return result


devidend, devisor = str(input("Введите числа через пробел (делимое, делитель): ")).split()
result_div = division(devidend, devisor)
if result_div is not None:
    print(f"{devidend} : {devisor} = {result_div}")
