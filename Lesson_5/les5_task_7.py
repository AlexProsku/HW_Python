"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

with open(file="./files/f_task7.txt", encoding="UTF-8", mode="r") as file:
    firm_profit = {}
    num_posit_prof = 0
    sum_posit_prof = 0
    for line in file:
        line_sp = line.split()
        profit = float(line_sp[2]) - float(line_sp[3])
        if profit > 0:
            sum_posit_prof += profit
            num_posit_prof += 1         # фирму с убытками не буду учитывать в подсчёте средней прибыли
        firm_profit.update({line_sp[0]: profit})
avg_profit = dict({"average_profit": round(sum_posit_prof / num_posit_prof, 2)})
firm_list = [firm_profit, avg_profit]
print(firm_list)

with open(file="./files/f_task7_new.json", mode="w") as file_json:
    json.dump(firm_list, file_json)
