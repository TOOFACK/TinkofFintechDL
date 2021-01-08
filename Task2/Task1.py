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
        temp_matrix = [[0 for x in range(9)] for y in range(9)]
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
        for row in self.field:
            for elem in row:
                if elem == 0:
                    print(" ", end='|')
                else:
                    print(elem, end='|')
            print()
            for i in range(18):
                print("_", end="")
            print()

    def update_field(self, row, col, point):
        found = False
        if self.field[row - 1][col - 1] != 0:
            print("This cell isnt empty, change position")
        else:

            if point not in self.field[row - 1]:
                for _row in self.field:
                    if _row[col - 1] == point:
                        found = True
                        break
                    else:
                        self.field[row - 1][col - 1] = point

            else:
                found = True

            if found:
                print("this value is already in the col or row, change it")
            else:
                self.print_field()

    def check_win(self):
        tr = True
        for row in self.field:
            for elem in row:
                if elem == 0:
                    tr = False
        if tr:
            print("Win!")
            return 1
        else:
            return 0


play = Main(int(input()))
play.create_field()
play.print_field()

while True:
    row = int(input())
    col = int(input())
    point = int(input())
    play.update_field(row, col, point)
    print()
    if play.check_win() == 1:
        break
    else:
        continue
