# 16/09/2026
# Matsenko Artemii
# task5

#todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.

def doall():
    x = float(input("Введите число x: "))
    y = float(input("Введите число y: "))
# Можно сделать выбор нужной операции:
#     operation = input("Выбор операции (+, -, /, *, //, %, **): ")
#     if operation == "+":
#         res = x + y
#     elif operation == "-":
#         res = x - y
#     elif operation == "/":
#         res = x / y
#     elif operation == "*":
#         res = x * y
#     elif operation == "//":
#         res = x // y
#     elif operation == "%":
#         res = x % y
#     elif operation == "**":
#         res = x ** y
#     print(f"{x} {operation} {y} = {res}")

# Либо без выбора, просто вывести все
    A = x + y
    B = x - y
    C = x / y
    D = x * y
    E = x // y
    F = x % y
    G = x ** y
    print("Сумма:", A,
          "\nРазность:", B,
          "\nДеление A на B:", C,
          "\nПроизведение:", D,
          "\nЦелая часть от деления A на B:", E,
          "\nОстаток от деления A на B:", F,
          "\nA в степени B:", G
          )
doall()