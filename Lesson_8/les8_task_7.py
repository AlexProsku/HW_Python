"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, comp_numb):
        self.comp_numb = comp_numb

    def __add__(self, other):
        return self.comp_numb + other.comp_numb

    def __mul__(self, other):
        return self.comp_numb * other.comp_numb

    def __str__(self):
        return f"{self.comp_numb}"


z1 = ComplexNumber(2+7j)
z2 = ComplexNumber(1-2j)
z3 = z1 + z2
z4 = z1 * z2
print(f"{z1} + {z2} = {z3}\tПроверка {(2+7j) + (1-2j)}")
print(f"{z1} * {z2} = {z4}\tПроверка {(2+7j) * (1-2j)}")
#
#
# # Ниже тщетно пытался изобрести велосипед - с выводом в методе __str__ затык случился
# class ComplexNumber2:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#
#
#     def __add__(self, other):
#         return ComplexNumber2(self.real + other.real, self.imag + other.imag)
#
#     def __mul__(self, other):
#         return ComplexNumber2((self.real * other.real + self.imag * other.imag),
#                               (self.imag * other.real + self.real * other.imag))
#
#     def __str__(self):
#         return f"{self.real}{self.imag}"
#         # if str(self.imag)[0] == "-":
#         #     return f"{self.real}{self.imag}"
#         #     # return f"{str(self.real).strip('0j')}{self.imag}"
#         #     # return f"{str(self.real).split('+')[0].split('(')[1]}{self.imag}"
#         # else:
#         #     return f"{self.real}+{self.imag}"
#         #     # return f"{str(self.real).strip('0j')}+{self.imag}"
#         #     # if str(self.real).split('(') == '':
#         #     #     return f"{str(self.real).split('+')[0].split('(')[1]}+{self.imag}"
#         #     # else:
#         #     #     return f"{self.real}+{self.imag}"
#
#
# z21 = ComplexNumber2(2, 7j)
# z22 = ComplexNumber2(1, -2j)
# z23 = z21 + z22
# z24 = z21 * z22
# print(f"{z21} + {z22} = {z23}")
# print(f"{z21} * {z22} = {z24}")
