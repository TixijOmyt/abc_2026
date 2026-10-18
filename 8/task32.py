# 15/10/2026
# Matsenko Artemii
# task32

# Инкапсуляция и property
# todo: Класс "Пользователь" (Валидация email)
# Создайте класс User. У него должны быть свойства email и password.
# При установке email проверяйте, что строка содержит символ @ (простая валидация).
# При установке пароля, храните не сам пароль, а его хеш (для простоты можно использовать hash()).
# Сделайте метод check_password(password), который проверяет, соответствует ли хеш переданного
# пароля сохраненному хешу.


class User:
    def __init__(self, email, password):
        self.email = email
        self.__password = hash(password)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Email должен содержать символ @")
        self.__email = value

    @property
    def password(self):
        raise AttributeError("Пароль недоступен для чтения")

    @password.setter
    def password(self, value):
        self.__password = hash(value)

    def check_password(self, password):
        return self.__password == hash(password)

# Пример использования
user = User("test@example.com", "secret")
print(user.email)  # test@example.com
# print(user.password) # AttributeError
print(user.check_password("secret"))  # True
print(user.check_password("wrong"))   # False