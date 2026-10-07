# 21/09/2026
# Matsenko Artemii
# task15

#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

mass = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ind = 0

for ind in mass:
    if ind == 11:
        break
    mass[ind-1] = mass[ind-1] + 1
    ind = ind + 1
print(mass)
