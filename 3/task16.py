# 21/09/2026
# Matsenko Artemii
# task16

# todo: База данных пользователя.
# Задан массив объектов пользователя

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе

# тип сортировки: 1

#Затем сообщение для ввода
# Ввидите критерии поиска: 16
#
# Результат:
#Пользователь: 'Piter' возраст 23 года, группа "admin"
#Пользователь: 'Dasha' возраст 30 лет, группа "master"

type_sort = input("Типы сортировки: "
                 "1 - по возрасту(больше введенного); "
                 "2 - по первой букве логина; 3 - по группе.\n"
                 "Введите тип: ")

if type_sort == "1":
    age = int(input("Введите критерий поиска: "))

    res = [user for user in users if user['age'] > age]
    res = sorted(res, key=lambda user: user['age'])

elif type_sort == "2":
    letter = input("Введите первую букву логина: ").lower()

    res = [
        user for user in users
        if user['login'][0].lower() == letter
    ]

elif type_sort == "3":
    group = input("Введите группу: ").lower()

    res = [
        user for user in users
        if user['group'].lower() == group
    ]

else:
    print("Неверный тип поиска!")
    res = []

print("\nРезультат:")

if res:
    for user in res:
        print(
        f"Пользователь: '{user['login']}' "
        f"возраст {user['age']} лет, "
        f"группа '{user['group']}'"
    )
else:
    print("Совпадений не найдено!")