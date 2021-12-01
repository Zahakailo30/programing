import random
def input_matrix(n):
    matrix = []
    for i in range(n):
        matr = []
        for j in range(n):
            matr.append(input_number("Введіть елемент:"))
        matrix.append(matr)
    print_matrix(matrix)

    return matrix


def check_size(n):
    if (n % 2 == 0):
        k = input_number("Помилка!Введіть непарне число:")
        n = check_size(k)
        return n
    elif (n < 0):
        k = input_number("Помилка!Введіть додатнє :")
        n = check_size(k)
        return n
    else:
        return n

def input_number(message):
    while True:
        try:
            print(message)
            n = int(input())
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
        n = input_number("Введіть порядок:")
        matrix1 = input_matrix(check_size(n))
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

