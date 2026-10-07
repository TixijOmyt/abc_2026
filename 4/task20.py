# 21/09/2026
# Matsenko Artemii
# task20

#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

#Содержимое файла inverted_sort.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

file = open("inverted_sort.txt", "r", encoding="utf-8")

lines = file.readlines()
file.close()

file = open("inverted_sort.txt", "a", encoding="utf-8")
file.write("\n\n")
for line in reversed(lines):
    file.write(line.rstrip() + "\n")

file.close()