import random as rdom


class Matrix:

    def __init__(self, matrix=None):
        if matrix is None:
            self.matrix = []
        else:
            self.matrix = matrix

    def get_matrix(self):
        return self.matrix


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
                num = int(input(f"Enter a number for row: {rows}, column: {columns}\n"))
                column.append(num)
            self.matrix.append(column)
        return self.matrix

    def add(self, matrix_2=None):
        result = []
        random = ""
        if matrix_2 is None:
            print("""* Remember for adding the row and coloumn have to be the same\n""")
            while random.lower() != "y" or random.lower() != "n":
                random = input("Do you want the matrix to be random (y/n)\n")
                if random.lower() == "y":
                    matrix_2 = Matrix().create(random=True, column=len(self.matrix), row=len(self.matrix[0]))
                else:
                    matrix_2 = Matrix().create(random=False, column=len(self.matrix), row=len(self.matrix[0]))

        for column in range(len(self.matrix)):
            temp = []
            for row in range(len(self.matrix[column])):
                temp.append(self.matrix[column][row] + matrix_2[column][row])
            result.append(temp)
        return Matrix(result)

    def sub(self, matrix_2=None):
        result = []
        random = ""
        if matrix_2 is None:
            print("""* Remember for subtracing the row and coloumn have to be the same\n""")
            while random.lower() != "y" or random.lower() != "n":
                random = input("Do you want the matrix to be random (y/n)\n")
                if random.lower() == "y":
                    matrix_2 = Matrix().create(random=True, column=len(self.matrix), row=len(self.matrix[0]))
                else:
                    matrix_2 = Matrix().create(random=False, column=len(self.matrix), row=len(self.matrix[0]))

        for column in range(len(self.matrix)):
            temp = []
            for row in range(len(self.matrix[column])):
                temp.append(self.matrix[column][row] - matrix_2[column][row])
            result.append(temp)
        return Matrix(result)

    def multiplication(self, matrix_2=None):
        result = []
        random = ""

        if matrix_2 is None:
            while random.lower() != "y" or random.lower() != "n":
                random = input("Do you want the matrix to be random (y/n)\n")
                if random.lower() == "y":
                    matrix_2 = Matrix().create(random=True, column=int(input("How many columns\n")),
                                               row=int(input("How many "
                                                             "rows\n")))
                else:
                    matrix_2 = Matrix().create(random=False, column=int(input("How many columns\n")),
                                               row=int(input("How many "
                                                             "rows\n")))

        if type(matrix_2) is int or type(matrix_2) is float:
            for col in range(len(self.matrix)):
                temp = []
                for row in range(len(self.matrix)):
                    temp += [matrix_2 * self.matrix[col][row]]
                result.append(temp)
            return Matrix(result)

        if len(self.matrix[0]) == len(matrix_2):
            for r_row in range(len(self.matrix)):
                temp = []
                for r_column in range(len(matrix_2[0])):
                    add_multi = sum(self.matrix[r_row][k] * matrix_2[k][r_column] for k in range(len(matrix_2)))
                    temp.append(add_multi)
                result.append(temp)
            return Matrix(result)


        else:
            raise ValueError("Matrix one must have the same number of columns as Matrix two has rows!")

    def get_sub_matrix(self, x: int, y: int) -> list:
        return [row[:y] + row[y + 1:] for row in (self.matrix[:x] + self.matrix[x + 1:])]

    def determinant(self):
        if len(self.matrix) != len(self.matrix[0]):
            raise ValueError("The Matrix needs to be a square")

        elif len(self.matrix) == 1 and len(self.matrix[0]) == 1:
            return self.matrix[0][0]

        elif len(self.matrix) == 2:
            return (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[0][1] * self.matrix[1][0])

        else:
            det = 0
            for row in range(len(self.matrix)):
                sub_matrix = Matrix(matrix=self.get_sub_matrix(x=0, y=row)).determinant()
                det += ((-1) ** row) * self.matrix[0][row] * sub_matrix
            return det

    def minor(self):

        if len(self.matrix) != len(self.matrix[0]):
            raise ValueError("The Matrix needs to be a square")

        else:
            minor = []
            for r in range(len(self.matrix)):
                temp = []
                for c in range(len(self.matrix)):
                    temp += [Matrix(self.get_sub_matrix(x=r, y=c)).determinant()]
                minor.append(temp)
            return minor

    def transpose(self):

        if len(self.matrix) != len(self.matrix[0]):
            raise ValueError("The matrix needs to be a square")

        ct = []
        for col in range(len(self.matrix)):
            temp = []
            for row in range(len(self.matrix)):
                temp += [self.matrix[row][col]]
            ct.append(temp)
        return ct

    def cofactors(self):
        print(self.matrix)

        if len(self.matrix) != len(self.matrix[0]):
            raise ValueError("Matrix needs to be a sqaure")

        else:
            result = []

            for row in range(len(self.matrix)):
                temp = []
                for col in range(len(self.matrix)):
                    temp += [((-1) ** (row + col)) * self.matrix[row][col]]
                result.append(temp)

            return result

    def inverse(self):
        if len(self.matrix) != len(self.matrix[0]):
            raise ValueError("Matrix has to be a square")

        if Matrix.determinant(self) == 0:
            raise ZeroDivisionError("The Matrix needs to be a non singular")

        if len(self.matrix) == 2:

            det = Matrix.determinant(self)
            self.matrix = Matrix.cofactors(self)
            self.matrix[0][0], self.matrix[1][1] = self.matrix[1][1], self.matrix[0][0]
            return self.multiplication(matrix_2=1 / det)

        else:
            det = Matrix.determinant(self)
            self.matrix = Matrix.minor(self)
            self.matrix = Matrix.cofactors(self)
            self.matrix = Matrix.transpose(self)
            return self.multiplication(matrix_2=1 / det)
