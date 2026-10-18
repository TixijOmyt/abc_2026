import random
import pickle
from db import get_collection

class PoleChudes:
    def __init__(self):
        self._dict = {}

        collection = get_collection()

        for word in collection.find():
            self._dict[word["word"]] = word["description"]

        keys = list(self._dict.keys())
        ind = random.randint(0, len(keys) - 1)
        self.secret = keys[ind]
        self.mask = [' * '] * len(self.secret)

    def show_describe(self):
        """ Выводит описание слова  """
        print(self._dict[self.secret])

    def show_secret(self):
        """ Выводит слово """
        for val in self.mask:
            print(val, end="")

    def get_letter(self):
        letter = input("\n Введите букву:")
        return letter

    def check_letter(self, letter):
        for ind, val in enumerate(self.secret):
            if val.upper() == letter.upper():
                self.mask[ind] = f" {letter} "

    def save_game(self):
        with open("save.pkl", "wb") as file:
            pickle.dump((self.secret, self.mask), file)
        print("Игра сохранена!")

    def load_game(self):
        try:
            with open("save.pkl", "rb") as file:
                self.secret, self.mask = pickle.load(file)
            print("Игра загружена!")
        except FileNotFoundError:
            print("Файл сохранения не найден!")

    def start(self):
        while (" * " in self.mask):
            self.show_describe()
            self.show_secret()
            letter = self.get_letter()

            if letter == "0":
                self.save_game()
                continue

            self.check_letter(letter)

game = PoleChudes()

if game.secret:
    answer = input("Загрузить сохранённую игру? (да/нет): ")

    if answer.lower() == "да":
        game.load_game()

    game.start()
