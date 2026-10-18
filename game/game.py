import  random


class PoleChudes:
    def __init__(self):
        self._dict = {
            'False': 'Логическое значение',
            'None': 'Пустой'
        }

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


    def start(self):
        while ( " * " in self.mask):
            self.show_describe()
            self.show_secret()
            letter = self.get_letter()
            self.check_letter(letter)

game = PoleChudes()
game.start()
