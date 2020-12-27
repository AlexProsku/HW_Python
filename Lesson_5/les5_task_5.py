"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open(file="./files/f_task5.txt", encoding="UTF-8", mode="wt") as file:
    num = "45 4 0 345 85 15.3"
    file.write(num)
with open(file="./files/f_task5.txt", encoding="UTF-8", mode="r") as file_r:
    file_r_list = file_r.readline().split()     # т.к. мы по заданию вводим 1 строку, то в цикле нет смысла читать файл
file_sum = 0
for el in file_r_list:
    file_sum += float(el)
print(f"Сумма чисел = {file_sum}")
