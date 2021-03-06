# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Для отладки:
# products_list = [
# (1, {"НазваниеТовара": "компьютер", "Цена": 20000, "Количество": 5, "ЕдиницаИзмерения": "шт"}),
# (2, {"НазваниеТовара": "принтер", "Цена": 6000, "Количество": 2, "ЕдиницаИзмерения": "шт"}),
# (3, {"НазваниеТовара": "сканер", "Цена": 2000, "Количество": 7, "ЕдиницаИзмерения": "шт"})
# ]

products_list = []
numb_item = 1
while True:
    products_item = list(str(input("Введите через пробел: "
                                   "\nназвание товара, цену, количество, единицу измерения (шт, кг, м) "
                                   "\nи нажмите Enter (ввод). "
                                   "\nДля завершения ввода товаров - введите END и/или нажмите Enter : ")
                             ).split())
    if products_item in [["END"], ["end"], []]:
        break
    products_dict = dict(НазваниеТовара=products_item[0], Цена=products_item[1], Количество=products_item[2],
                         ЕдиницаИзмерения=products_item[3])
    products_tuple = numb_item, products_dict
    products_list.append(products_tuple)
    numb_item += 1
print("Структура данных Товары:")
print(*products_list, sep='\n')
products_name, price, quantity, measure = [], [], [], []
for i in products_list:
    products_name.append(i[1].get('НазваниеТовара'))
    price.append(i[1].get('Цена'))
    quantity.append(i[1].get('Количество'))
    measure.append(i[1].get('ЕдиницаИзмерения'))
analitics = dict(НазваниеТовара=(list(set(products_name))), Цена=(list(set(price))),
                 Количество=(list(set(quantity))), ЕдиницаИзмерения=(list(set(measure))))
print("Аналитика:")
print(str(analitics).replace('], ', '],\n'))     # с f строкой не придумал как сделать, что отображалось как в примере.
# print(*analitics, sep='\n')
# В последнем закоменченном print съедаются значения из словаря - подозреваю из-за разных типов данных (строка и список)
