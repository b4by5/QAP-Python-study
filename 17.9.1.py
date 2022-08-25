sequence = '9 5 3 7 4 8 1 2 23 31 11'
_list = list(map(int, sequence.split()))

try:
    num = int(input('Введите любое число: '))
except ValueError:
    raise Exception('Условие ввода данных не соблюдено!')


def binary_search(array, num, left, right):
    try:
        if left > right:
            return False

        middle = (right + left) // 2
        if array[middle] < num <= array[middle + 1]:
            return middle
        elif num > array[middle]:
            return binary_search(array, num, left + 1, right)
        else:
            return binary_search(array, num, left, right - 1)

    except IndexError:
        raise Exception('Введенное число выходит за пределы последовательности')


def bubble():
    global _list
    for i in range(len(_list)):
        for j in range(len(_list) - i - 1):
            if _list[j] > _list[j + 1]:
                _list[j], _list[j + 1] = _list[j + 1], _list[j]
    print(_list)
    return _list


array = _list

bubble()
print(binary_search(array, num, 0, len(_list)))
