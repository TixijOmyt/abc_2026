# 11/10/2026
# Matsenko Artemii
# task28

#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

import re

inp = input()

def replace(match):
    n = int(match.group())
    if n == 0:
        return ' '
    if 1 <= n <= 26:
        return chr(ord('a') + (n - 1))
    return match.group()

result = re.sub(r'\d+', replace, inp)

result = re.sub(r'(?<=[a-z]) +(?=[a-z])', '', result)
result = re.sub(r'\s+([,.!?;:])', r'\1', result)
result = re.sub(r' {2,}', ' ', result).strip()

print(result)