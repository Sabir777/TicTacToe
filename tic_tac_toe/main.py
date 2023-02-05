import random
import time

class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return not bool(self.value)


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.all_cell = lambda: ((i, j) for i in range(3) for j in range(3))
        self.init()

    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        self.busy = []

    @staticmethod
    def check_indx(i, j):
        if not (isinstance(i, int) and isinstance(j, int) and 0 <= i < 3 and 0 <= j < 3):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        i, j = item
        self.check_indx(i, j)
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        i, j = key
        self.check_indx(i, j)
        self.pole[i][j].value = value

    def __iter__(self):
        return (col for row in self.pole for col in row)

    def show(self):
        for row in self.pole:
            print(*(col.value for col in row))

    def human_go(self):
        print('___________________________________________________________________')
        coords = input('Сделайте ход. Введите координаты клетки через пробел'
                       '\nПервая координата - номер строки. Вторая координата - номер столбца'
                       '\nВвод данных: ')
        while True:
            try:
                i, j = map(int, coords.split())
                if not self.pole[i][j]:
                    coords = input('Вы ввели неверные координаты. Эта клетка занята'
                                    '\nВведите координаты свободной клетки через пробел'
                                   '\nВвод данных: ')
                else:
                    self.pole[i][j].value = TicTacToe.HUMAN_X
                    self.busy.append((i, j))
                    break
            except:
                coords = input('Вы ввели некорректные данные. Попробуйте еще раз. '
                               '\nКоординатами могут быть числа от 0 до 2.'
                               '\nВведите координаты свободной клетки'
                               '\nВвод данных: ')
        print('___________________________________________________________________')

    def computer_go(self):
        print('___________________________________________________________________')
        print('Компьютер думает...')
        i, j = random.choice(list(set(self.all_cell()) - set(self.busy)))
        self.pole[i][j].value = TicTacToe.COMPUTER_O
        self.busy.append((i, j))
        time.sleep(2)
        print('___________________________________________________________________')

t = TicTacToe()

while True:
    t.show()
    t.human_go()
    t.show()
    t.computer_go()
