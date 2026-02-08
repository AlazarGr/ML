from random import randint
def printMatrix(matrix):
    text = "{} "*len(matrix[0])
    for row in matrix:
        print(text.format(*row))

n, m = randint(1, 10), randint(1, 10)
matrix = [[randint(20,80) for _ in range(m)] for _ in range(n)]
printMatrix(matrix)