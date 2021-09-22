import random

def move_max_el(n):
    if(n % 2 == 0):
        print("Введіть непарне число!")
    elif(n < 0):
        print("Введіть додатнє число!")
    else:
        matrix = []
        for i in range(n):
            matr = []
            for j in range(n):
                matr.append(random.randrange(0, 100))
            matrix.append(matr)

        def print_m(matrix):
            k = len(matrix)
            for i in range(k):
                for j in range(k):
                    print(matrix[i][j], end=' ')
                print()
            print(' ')
        print_m(matrix)


        i1 = 0
        j1 = 0
        max = matrix[0][0]
        for i in range(n):
            for j in range(n):
                if (i == j or j == n - i - 1):
                    if (max < matrix[i][j]):
                        max = matrix[i][j]
                        i1 = i
                        j1 = j

        print("Найбільший елемент головної і бічної діагональ: ", max)

        temp = matrix[n // 2][n // 2]
        matrix[n // 2][n // 2] = matrix[i1][j1]
        matrix[i1][j1] = temp

        print_m(matrix)



try:
    n = int(input('Введіть порядок: '))
    move_max_el(n)
except TypeError:
    print("Помилка!")
except Exception:
    print("Помилка!")

