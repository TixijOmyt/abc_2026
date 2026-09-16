# 16/09/2026
# Matsenko Artemii
# task11

#  todo: Дан номер месяца (1 — январь, 2 — февраль, ...). Вывести название соответствующего
#  времени года ("зима", "весна" и т.д.).

num = int(input("Введите номер месяца: "))

if num == 1 or num == 2 or num == 12:
    print("Время года - зима")
elif num == 3 or num == 4 or num == 5:
    print("Время года - весна")
elif num == 6 or num == 7 or num == 8:
    print("Время года - лето")
elif num == 9 or num == 10 or num == 11:
    print("Время года - осень")
else:
    print("А название месяцу придумал?")