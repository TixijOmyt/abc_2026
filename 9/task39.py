class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def name(self):
      return self._name

    @name.setter
    def name(self, name):
      self._name = name
  
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if price < 0:
            self._price = 0
        else:
            self._price = price


class Order:
    def __init__(self):
        self.products = []

    @property
    def total_price(self):
        return sum(product.price for product in self.products)

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

book = Product("Book", 10)
pen = Product("Pen", 2)
order = Order()
order.add_product(book)
order.add_product(pen)
print(order.total_price)