def reverseNegativeNumbers(array):
    negative = []
    negative_count = 0
    negative_size = 0
    n = len(array)
    for i in range(n):
        if array[i] < 0:
            negative.append(array[i])
            negative_size += 1
    for i in range(n):
        if array[i] >= 0:
            continue
        array[i] = negative[negative_size - negative_count - 1]
        negative_count += 1
    print(array)
    return array


def input_array():
    n = int(input("Введіть розмір масиву: "))
    array = []

    for i in range(n):
        a = int(input("Введіть елемент масиву: "))
        array.append(a)
    print(array)
    return array

try:
   array = input_array()
   reverseNegativeNumbers(array)
except ValueError:
    print("Використано не відповідний тип даних")
except Exception:
    print("Помилка!")