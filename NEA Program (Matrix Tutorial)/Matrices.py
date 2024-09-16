import random as rdom


class Matrix:

    def __init__(self, matrix=None):
        if matrix is None:
            self.matrix = []
        else:
            self.matrix = matrix

    def create(self, random: bool = False, column: int = None, row: int = None) -> list:
        if random is True:
            return self.random_matrix(column, row)
        else:
            return self.manual_matrix(column, row)

    def random_matrix(self, r: int, c: int) -> list:
        self.matrix = []
        if r is None:
            r = rdom.randint(1, 3)
        if c is None:
            c = rdom.randint(1, 3)

        for row in range(r):
            column = []
            for col in range(c):
                column.append(rdom.randint(0, 9))
            self.matrix.append(column)
        return self.matrix

    def manual_matrix(self, r: int, c: int) -> list:
        self.matrix = []
        for rows in range(1, r + 1):
            column = []
            for columns in range(1, c + 1):
                num = int(input(f'Enter a number for row: {rows}, column: {columns}\n'))
                column.append(num)
            self.matrix.append(column)
        return self.matrix

    def add(self, matrix_2: list = None) -> list:
        result = []
        random = ""
        if matrix_2 is None:
            print('''* Remember for adding the row and coloumn have to be the same\n''')
            while random.lower() != "y" or random.lower() != "n":
                random = input('Do you want the matrix to be random (y/n)\n')
                if random.lower() == 'y':
                    matrix_2 = Matrix().create(random=True, column=len(self.matrix), row=len(self.matrix[0]))
                else:
                    matrix_2 = Matrix().create(random=False, column=len(self.matrix), row=len(self.matrix[0]))

        for column in range(len(self.matrix)):
            temp = []
            for row in range(len(self.matrix[column])):
                temp.append(self.matrix[column][row] + matrix_2[column][row])
            result.append(temp)
        return result

    def sub(self, matrix_2: list = None) -> list:
        result = []
        random = ""
        if matrix_2 is None:
            print('''* Remember for subtracing the row and coloumn have to be the same\n''')
            while random.lower() != "y" or random.lower() != "n":
                random = input('Do you want the matrix to be random (y/n)\n')
                if random.lower() == 'y':
                    matrix_2 = Matrix().create(random=True, column=len(self.matrix), row=len(self.matrix[0]))
                else:
                    matrix_2 = Matrix().create(random=False, column=len(self.matrix), row=len(self.matrix[0]))

        for column in range(len(self.matrix)):
            temp = []
            for row in range(len(self.matrix[column])):
                temp.append(self.matrix[column][row] - matrix_2[column][row])
            result.append(temp)
        return result

    def multiplication(self, matrix_2: list = None) -> list:
        result = []
        random = ""

        if matrix_2 is None:
            while random.lower() != "y" or random.lower() != "n":
                random = input('Do you want the matrix to be random (y/n)\n')
                if random.lower() == 'y':
                    matrix_2 = Matrix().create(random=True, column=int(input('How many columns\n')),
                                               row=int(input('How many '
                                                             'rows\n')))
                else:
                    matrix_2 = Matrix().create(random=False, column=int(input('How many columns\n')),
                                               row=int(input('How many '
                                                             'rows\n')))

        if len(self.matrix[0]) == len(matrix_2):
            for r_row in range(len(self.matrix)):
                temp = []
                for r_column in range(len(matrix_2[0])):
                    add_multi = sum(self.matrix[r_row][k] * matrix_2[k][r_column] for k in range(len(matrix_2)))
                    temp.append(add_multi)
                result.append(temp)
            return result

        else:
            print('Matrix one must have the same number of columns as Matrix two has rows!')
            return []

    def get_sub_matrix(self, x: int, y: int) -> list:
        return [row[:y] + row[y + 1:] for row in (self.matrix[:x] + self.matrix[x + 1:])]

    def determinant(self):
        if len(self.matrix) == 2:
            return (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[0][1] * self.matrix[1][0])

        elif len(self.matrix) == 3:
            det = 0
            for row in range(len(self.matrix)):
                sub_matrix = Matrix(matrix=self.get_sub_matrix(x=0, y=row)).determinant()
                det += ((-1) ** row) * self.matrix[0][row] * sub_matrix
            return det
        else:
            return "Matrix has to be a 3x3 or a 2x2"
