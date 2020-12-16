# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

work_hours, sal_per_hour, sal_bonus = float(argv[1]), float(argv[2]), float(argv[3])
salary_summ = work_hours * sal_per_hour + sal_bonus
print(salary_summ)
