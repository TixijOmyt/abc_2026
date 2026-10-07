# 21/09/2026
# Matsenko Artemii
# task19

#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# id) - номер по порядку (от 1 до 10);
# значение из списка algoritm

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" ,
             "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
             "Наивный байесовский классификатор", "CART" ]

# for i in algoritm:
#     print(i)
#     file
# Каждое значение из списка должно находится на отдельной строке.
# Пример файла algoritm.csv:
# 1) "C4.5"
# 2) "k - means"
# .....

file = open("algoritm.csv", "w", encoding="utf-8")

str_id = 1
for i in algoritm:
    file.write(f'{str_id}) "{i}"\n')
    str_id += 1

file.close()