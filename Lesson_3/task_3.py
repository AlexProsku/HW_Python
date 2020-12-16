# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def sum_max_arg(a, b, c):
    arguments = a, b, c
    arguments = sorted(list(arguments))
    return arguments[-1] + arguments[-2]


arg1, arg2, arg3 = 4, 98, 2
print(f"Сумма наибольших двух аргументов = {sum_max_arg(arg1, arg2, arg3)}")
