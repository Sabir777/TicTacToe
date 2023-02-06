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
        self.all_cell = None
        self.pole = None
        self.init()

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


cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
print(game.is_human_win)
# assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"
#
# game[0, 0] = TicTacToe.HUMAN_X
# game[1, 1] = TicTacToe.HUMAN_X
# game[2, 2] = TicTacToe.HUMAN_X
# assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
#
# game.init()
# game[0, 0] = TicTacToe.COMPUTER_O
# game[1, 0] = TicTacToe.COMPUTER_O
# game[2, 0] = TicTacToe.COMPUTER_O
# assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

