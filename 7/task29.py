# 11/10/2026
# Matsenko Artemii
# task29

#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
#
#
# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

for shift in range(26):
    result = ""
    for char in text:
        if char.isalpha():
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char
    print(f"Сдвиг {shift:2}: {result}")