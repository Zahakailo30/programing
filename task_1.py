def func():
    negative = []
    negative_count = 0
    negative_size = 0

    n = int(input("Введіть розмір масиву: "))
    array = []
    for i in range(n):
        a = int(input("Введіть елемент масиву: "))
        array.append(a)
        if a < 0:
            negative.append(a)
            negative_size += 1

    for i in range(n):
        if array[i] >= 0:
            continue
        array[i] = negative[negative_size - negative_count - 1]
        negative_count += 1

    print(array)

try:
    func()
except ValueError:
    print("Використано не відповідний тип даних")
except Exception:
    print("Помилка!")

