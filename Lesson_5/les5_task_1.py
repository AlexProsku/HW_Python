"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

f = open(file="./files/f_task1.txt", encoding="UTF-8", mode="wt")
try:
    while True:
        f_str = input("Введите текст и нажмите Enter (для выхода нажмите Enter без ввода текста): ") + "\n"
        if f_str == '\n':
            break
        else:
            f.write(f_str)
finally:
    f.close()
