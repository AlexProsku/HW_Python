"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

def gen_fa(numb):
    rez = 1
    while rez <= numb:
        yield rez
        rez += 1
"""
n -переменная с числом, от которого будем считать факториал. Работает с 0, т.к. задаю начальное значение fact_n = 1
"""
n = 4
fact_n = 1
for i in gen_fa(n):
    fact_n *= i
print(f"{n}! = {fact_n}")
