"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open(file="./files/f_task3.txt", encoding="UTF-8", mode="r") as file:
    staf_lowsal = []
    sum_salary = 0
    staf_quan = 0
    for line in file:
        line_sp = line.split()
        salary_line = float(line_sp[1])
        sum_salary += salary_line
        staf_quan += 1
        if salary_line < 20000:
            staf_lowsal.append(line_sp[0])
print(f"Сотрудники с доходом менее 20 тыс: {', '.join(staf_lowsal)}")
print(f"Средний доход = {sum_salary / staf_quan}")
