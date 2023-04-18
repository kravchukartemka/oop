# test
class Matrix:
    meaning = []

    def __init__(self):
        n = int(input("Enter n:\n"))
        m = int(input("Enter m:\n"))
        self.meaning = [[int(input()) for i in range(m)] for j in range(n)]

    def __add__(self, obj2):
        matrix_one = self.meaning
        matrix_two = obj2.meaning
        if ((matrix_one[0] != matrix_two[0]) or (len(matrix_one) != len(matrix_two))):
            print("incorrect dimension")
        else:
            result = [[matrix_one[i][j] + matrix_two[i][j] for j in range(len(matrix_one[0]))] for i in range(len(matrix_one))]
            self.meaning = result

    def __mul__(self, obj2):
        matrix_one = self.meaning
        matrix_two = obj2.meaning
        if ((len(matrix_one[0]) != len(matrix_two)) or (len(matrix_one) != len(matrix_two[0]))):
            print("incorrect dimension")
        else:
            length = len(matrix_one)
            result_matrix = [[0 for i in range(length)] for i in range(length)]
            for i in range(length):
                for j in range(length):
                    for k in range(length):
                        result_matrix[i][j] += matrix_one[i][k] * matrix_two[k][j]
            self.meaning = result_matrix

    def __str__(self):
        print("Matrix:\n")
        matrix_one = self.meaning
        for i in range(len(matrix_one[0])):
            s = ""
            for j in range(len(matrix_one)):
                s += str(matrix_one[i][j]) + " "
            print(s)

if __name__ == '__main__':
    matrix1 = Matrix()
    matrix2 = Matrix()
    matrix1.__mul__(matrix2)
    matrix1.__str__()
    matrix1.__add__(matrix2)
    matrix1.__str__()
