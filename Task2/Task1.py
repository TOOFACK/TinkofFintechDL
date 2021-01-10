import os
from random import randint
import pickle as pk


class Main(object):
    field = [[0 for x in range(9)] for y in range(9)]
    points = 0

    def __init__(self, points):
        self.points = points
        self.field = [[(int)((i * 3 + i / 3 + j) % (9) + 1) for j in range(9)] for i in range(9)]

    def transpon(self):
        matrix = list(self.field)
        temp_list = []
        for j in range(9):
            for i in range(9):
                temp_list.append(self.field[i][j])
            matrix[j] = list(temp_list)
            temp_list.clear()
        self.field = matrix.copy()

    def swap_row(self):
        index1 = randint(0, 8)
        index2 = randint(0, 8)
        if index2 == index1:
            while index2 != index1:
                index1 = randint(0, 8)
                index2 = randint(0, 8)
        temp_list = self.field[index1]
        self.field[index1] = self.field[index2]
        self.field[index2] = temp_list

    def swap_col(self):
        self.transpon()
        self.swap_row()
        self.transpon()

    def create_field_utils(self):
        self.swap_row()
        self.swap_col()

    def create_field(self):

        temp = randint(1, 25)
        for j in range(temp):
            self.create_field_utils()
        temp_matrix = [[0 for _ in range(9)] for _ in range(9)]
        k = 0
        while k < self.points:
            k += 1
            i = randint(0, 8)
            j = randint(0, 8)
            if temp_matrix[i][j] != 0:
                while True:
                    i = randint(0, 8)
                    j = randint(0, 8)
                    if temp_matrix[i][j] == 0:
                        break

            temp_matrix[i][j] = self.field[i][j]
        else:
            temp_matrix[i][j] = self.field[i][j]
        self.field = list(temp_matrix)

    def print_field(self):
        for _row in self.field:
            for elem in _row:
                if elem == 0:
                    print(" ", end='|')
                else:
                    print(elem, end='|')
            print()
            for i in range(18):
                print("_", end="")
            print()

    def update_field(self, _row, _col, _point):
        found = False
        if self.field[_row - 1][_col - 1] != 0:
            print("This cell isnt empty, change position")
        else:

            if point not in self.field[_row - 1]:

                for _1row in self.field:
                    if _1row[_col - 1] == point:
                        print("1")
                        found = True
                        break
            else:
                found = True

            if found:
                print("this value is already in the col or row, change it")
            else:
                self.field[_row - 1][_col - 1] = point
                self.print_field()

    def check_win(self):
        _tr = True
        for _row in self.field:
            for elem in _row:
                if elem == 0:
                    _tr = False
        if _tr:
            print("Win!")
            return 1
        else:
            return 0

    def save(self):
        f = open('input.txt', 'wb')
        pk.dump(self, f)
        f.close()

was_saved = True
try:
    file = open('input.txt', 'rb')
except IOError as e:
    print("Starting a new game...")
    was_saved = False
else:
    with file:
        print("Open saved game...")
        play = pk.load(file)
        play.print_field()
        tr = False
        print("If you want ot leave input -1 -1 -1")
        if play.check_win() == 1:
            tr = True
        else:
            tr = False
        while True and not tr:
            row = int(input())
            col = int(input())
            point = int(input())
            if row == -1 and col == -1 and point == -1:
                print("Saving...")
                play.save()
                break

            while 10 < row or row < 0 or 10 < col or col < 0 or 9 < point or point < 0:
                print("check your input its wrong")
                row = int(input())
                col = int(input())
                point = int(input())

            play.update_field(row, col, point)

            if play.check_win() == 1:
                os.remove('input.txt')
                break
            else:
                continue
if not was_saved:
    p = int(input())
    while 80 < p  or p < 0:
        print("change start amount of points")
        p = int(input())
    play = Main(p)
    play.create_field()
    play.print_field()
    tr = False
    print("If you want ot leave input -1 -1 -1")
    if play.check_win() == 1:
        tr = True
    else:
        tr = False
    while True and not tr:
        row = int(input())
        col = int(input())
        point = int(input())
        if row == -1 and col == -1 and point == -1:
            print("Saving...")
            play.save()
            break

        while 10 < row or row < 0 or 10 < col or col < 0 or 9 < point or point < 0:
            print("check your input its wrong")
            row = int(input())
            col = int(input())
            point = int(input())

        play.update_field(row, col, point)

        if play.check_win() == 1:
            break
        else:
            continue




