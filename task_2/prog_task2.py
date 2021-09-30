import random
def input_matrix(n):
    while True:
        try:
            matrix = []
            for i in range(n):
                matr = []
                for j in range(n):
                    matr.append(int(input("Введіть елемент:\n")))
                matrix.append(matr)
            print_matrix(matrix)
            break
        except ValueError:
            print("Неправильний тип!")
    return matrix

def input_number():
    while True:
        try:
            n = int(input('Введіть порядок: '))
            if (n % 2 == 0):
                print("Введіть непарне число!")
                continue
            elif (n < 0):
                print("Введіть додатнє число!")
                continue
            break
        except ValueError:
            print("Неправильний тип")
    return n

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


print("Оберіть опцію:\n 1 - виконати завдання \n 2 - завершити роботу \n", end=" ")
P = int(input(""))
while P:
    if P == 1:
        n = input_number()
        matrix1 = input_matrix(n)
        move_max_el(matrix1)
        print("Оберіть опцію:\n 1 - виконати завдання \n 2 - завершити роботу \n", end=" ")
        P = int(input(""))
    elif P == 2:
        print("Роботу завершено")
        break
    elif P > 2 or P < 0:
        print("Такої опції не існує!")
        print("Оберіть опцію:\n 1 - виконати завдання \n 2 - завершити роботу \n", end=" ")
        P = int(input(""))
