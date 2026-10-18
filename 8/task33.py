# 15/10/2026
# Matsenko Artemii
# task33

# Инкапсуляция и property
# todo: Класс "Товар" (Защита от отрицательной цены)
# Создайте класс Product. У него есть свойства name (простая строка) и price.
# При установке цены проверяйте, что она не отрицательная.
# Если пытаются установить отрицательную цену, устанавливайте 0.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            self._price = 0
        else:
            self._price = new_price

# Пример использования
product = Product("Book", 10)
print(product.price)  # 10
product.price = -5
print(product.price)  # 0