"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

with open(file="./files/f_task2.txt", encoding="UTF-8", mode="r") as file:
    for num, line in enumerate(file, start=1):
        print(f"Строка {num} содержит слов - {len(line.split())}")
