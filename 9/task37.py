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

user = User("test@example.com", "secret")
print(user.email)
print(user.check_password("secret"))
print(user.check_password("wrong"))