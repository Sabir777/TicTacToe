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

    def init(self):
        self.all_cell = [(i, j) for i in range(3) for j in range(3)]
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

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

    def is_win(self, val):
        it1 = [(i, i) for i in range(3)]
        it2 = [(i, 2 - i) for i in range(3)]
        it3 = [[(i, j) for j in range(3)] for i in range(3)]
        it4 = [[(i, j) for i in range(3)] for j in range(3)]
        lst_it = [it1, it2, *it3, *it4]
        for it in lst_it:
            if all(self.pole[i][j].value == val for i, j in it):
                return True
        return False

    @property
    def is_human_win(self):
        return self.is_win(self.HUMAN_X)

    @property
    def is_computer_win(self):
        return self.is_win(self.COMPUTER_O)

    @property
    def is_draw(self):
        return not (self.is_human_win or self.is_computer_win)

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
                    self.all_cell.remove((i, j))
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
        time.sleep(2)
        i, j = random.choice(self.all_cell)
        self.pole[i][j].value = TicTacToe.COMPUTER_O
        self.all_cell.remove((i, j))
        print('___________________________________________________________________')

    def __bool__(self):
        return self.is_draw and bool(self.all_cell)


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")

# t = TicTacToe()
#
# while True:
#     t.show()
#     t.human_go()
#     t.show()
#     t.computer_go()
