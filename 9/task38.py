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
          
product = Product("Book", 10)
print(product.price)
product.price = -5
print(product.price)