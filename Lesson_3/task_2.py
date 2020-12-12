# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data_input():
    user_data_dict = {}
    print("Вводите данные пользователя через ENTER:\nФамилия, Имя, ГодРождения, ГородПроживания, email, "
          "Телефон")
    for userKey in ['Фамилия', 'Имя', 'ГодРождения', 'ГородПроживания', 'email', 'Телефон']:
        print(f"Введите значение поля {userKey}:")
        user_data_dict.update({userKey: str(input())})
    return user_data_dict


def user_data_print(first_name_p, lastname_p, birth_date_p, residence_city_p, email_p, phone_p):
    print(f"{first_name_p} {lastname_p}, {birth_date_p} года рождения. Проживает в городе {residence_city_p}. "
          f"Контакты: email: {email_p}, телефон: {phone_p}")


user_data = user_data_input()
user_data_print(first_name_p=user_data.get('Имя'), lastname_p=user_data.get('Фамилия'),
                birth_date_p=user_data.get('ГодРождения'), residence_city_p=user_data.get('ГородПроживания'),
                phone_p=user_data.get('Телефон'), email_p=user_data.get('email'))
