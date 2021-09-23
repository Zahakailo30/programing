import random
def input_matrix():
    n = int(input('Введіть порядок: '))
    if (n % 2 == 0):
        print("Введіть непарне число!")
    elif (n < 0):
        print("Введіть додатнє число!")
    else:
        matrix = []
        for i in range(n):
            matr = []
            for j in range(n):
                matr.append(int(input("Введіть елемент:\n")))
            matrix.append(matr)

        print_matrix(matrix)
        return matrix
def print_matrix(matrix):
    k = len(matrix)
    for i in range(k):
        for j in range(k):
            print(matrix[i][j], end=' ')
        print()
    print(' ')
def move_max_el(matrix):
    i1 = 0
    j1 = 0
    n = len(matrix)
    max = matrix[0][0]
    for i in range(n):
        for j in range(n):
            if (i == j or j == n - i - 1):
                if (max < matrix[i][j]):
                    max = matrix[i][j]
                    i1 = i
                    j1 = j

    temp = matrix[n // 2][n // 2]
    matrix[n // 2][n // 2] = matrix[i1][j1]
    matrix[i1][j1] = temp

    print_matrix(matrix)
    return matrix

try:
    print("Оберіть опцію:\n 1 - виконати завдання \n 2 - завершити роботу \n", end=" ")
    P = int(input(""))
    while (P == 1):
        matrix1 = input_matrix()
        move_max_el(matrix1)
        print("Оберіть опцію:\n 1 - виконати завдання \n 2 - завершити роботу \n", end=" ")
        P = int(input(""))
    if (P == 2):
        print("Роботу завершено")

except ValueError:
    print("Неправильний тип даних!")
except Exception:
    print("Помилка!")