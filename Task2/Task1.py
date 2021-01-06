from random import randint


class Main(object):
    field = [[0 for x in range(9)] for y in range(9)]
    points = 0

    def __init__(self, points):
        self.points = points

    def create_field(self):
        amount_of_points = self.points
        while amount_of_points > 0:
            point = randint(1, 9)
            i = randint(0, 8)
            j = randint(0, 8)
            self.field[i][j] = point
            amount_of_points = amount_of_points-1


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
