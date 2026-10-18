def caesar_crypt(filename):
    lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    upper = lower.upper()

    with open(filename, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file, 1):
            result = ''

            for char in line:
                if char in lower:
                    result += lower[(lower.index(char) - i) % 33]
                elif char in upper:
                    result += upper[(upper.index(char) - i) % 33]
                else:
                    result += char

            print(result, end='')
