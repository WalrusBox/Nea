import random as rdom


class matrix:  # Creating and returning a matrix

    def __init__(self):
        self.matrix = []

    def create(self, random: bool = False, row: int = None, column: int = None) -> list:  # return the matrix
        if random is True:
            return self.random_matrix(row, column)
        else:
            return self.manuel_matrix(row, column)

    def random_matrix(self, r: int, c: int) -> list:  # random matrix creater 2000
        self.matrix = []
        if r is None:  # if row isn't define
            r = rdom.randint(1, 3)  # how many rows it will have
        if c is None:
            c = rdom.randint(1, 3)  # how many columns it will have

        for row in range(r):  # Row
            column = []
            for col in range(c):  # column
                column.append(rdom.randint(0, 9))
            self.matrix.append(column)
        return self.matrix

    def manuel_matrix(self, r: int, c: int) -> list:
        self.matrix = []
        for rows in range(1, r+1):
            column = []
            for columns in range(1, c+1):
                num = int(input(f'Enter a number for row: {rows}, column: {columns}\n'))
                column.append(num)
            self.matrix.append(column)
        return self.matrix


class ajnop''