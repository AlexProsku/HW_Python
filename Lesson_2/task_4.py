# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

string_input = str(input("Введите несколько слов через пробел: ")).split()
for numb, el in enumerate(string_input, start=1):
    print(f"{numb}. {el[:10]}")