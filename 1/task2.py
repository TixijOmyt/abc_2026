# 14/09/2026
# Matsenko Artemii
# task2

# todo: Преобразуйте переменную age и foo в число

age = "23"
foo = "23abc"

age = int(age)
print("(1.1)Переменная age имеет тип", type(age), "и равняется age =", age)
# Тут есть 2 варианта:
# 1) foo - это строка типа число 23 + буквенная запись "abc". Её нельзя преобразовать в int напрямую,
# поэтому остается обрезать буквенную часть
foo = int(foo[:2])
print("(1.2.1)Переменная foo имеет тип", type(foo), "и равняется foo =", foo)
# 2) 23abc можно представить как число, записанное в шестнадцатеричной системе счисления, тогда
foo = "23abc"
foo = int(foo, 16)
print("(1.2.2)Переменная foo имеет тип", type(foo), "и равняется foo =", foo)

# Преобразуйте переменную age в Boolean
age = "123abc"
age = bool(age)
print("(2)Переменная age имеет тип", type(age), "и принимает значение age =", age)

# Преобразуйте переменную flag в Boolean
flag = 1
flag = bool(flag)
print("(3)Переменная flag имеет тип", type(flag), "и принимает значение flag =", flag)

# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""

str_one = bool(str_one)
str_two = bool(str_two)

print("(4.1)Переменная str_one имеет тип", type(str_one), "и принимает значение str_one =", str_one)
print("(4.2)Переменная str_two имеет тип", type(str_two), "и принимает значение str_two =", str_two)

# Преобразуйте значение 0 и 1 в Boolean
x = bool(0)
y = bool(1)

print("(5.1)Переменная x имеет тип", type(x), "и принимает значение x =", x)
print("(5.2)Переменная y имеет тип", type(y), "и принимает значение y =", y)

# Преобразуйте False в строку
false_string = str(False)
print("(6)Переменная false_string имеет тип", type(false_string),
      "и принимает значение false_string =", false_string)