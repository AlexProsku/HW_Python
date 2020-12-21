"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
file = open(file="./files/f_task4.txt", encoding="UTF-8", mode="r")
file_new = open(file="./files/f_task4_new.txt", encoding="UTF-8", mode="wt")
try:
    for line in file:
        line = line.split()
        line[0] = translate.get(line[0])
        file_new.write((' '.join(line)) + '\n')
finally:
    file.close()
    file_new.close()
