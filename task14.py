# 21/09/2026
# Matsenko Artemii
# task14

#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !
#Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
#
# for ind in mass:
#
#
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.
#
mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]

last_index = {}
min_distance = {}
result = {}

for ind, val in enumerate(mass):
    if val in last_index:
        distance = ind - last_index[val]

        # Если это первая найденная пара или расстояние меньше предыдущего
        if val not in min_distance or distance < min_distance[val]:
            min_distance[val] = distance
            result[val] = (last_index[val], ind)

    last_index[val] = ind
    # print(last_index)
    # print(result)

for val in result:
    print(
        f"Для числа {val} минимальное расстояние в массиве"
        f" по индексам {result[val][0]} и {result[val][1]}, "
    )