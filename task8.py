# 16/09/2026
# Matsenko Artemii
# task8

# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково слева направо и справа налево".

num = int(input("Введите четырехзначное число: "))

thousand = num // 1000
hundred = (num % 1000) // 100
ten = (num % 100) // 10
unit = (num % 10)

if thousand == unit and hundred == ten:
    print("True")
else:
    print("False")
