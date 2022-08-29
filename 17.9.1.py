sequence = '9 5 3 7 4 8 1 2 23 31 11'
_list = list(map(int, sequence.split()))

try:
    number = int(input(f'Введите число от {min(_list)+1} до {max(_list)}: '))
except ValueError:
    raise Exception('Условие ввода данных не соблюдено!')


def bubble():
    global _list
    for i in range(len(_list)):
        for j in range(len(_list) - i - 1):
            if _list[j] > _list[j + 1]:
                _list[j], _list[j + 1] = _list[j + 1], _list[j]
    return _list


def binary_search(array, num, left, right):
    if left >= right:
        return f'Введенное число выходит за пределы последовательности {_list}'

    middle = (right + left) // 2
    if array[middle] < num <= array[middle + 1]:
        return middle
    elif num > array[middle]:
        return binary_search(array, num, left + 1, right)
    else:
        return binary_search(array, num, left, right - 1)


print(f'Список: {bubble()}')
print(f'Позиция в списке: {binary_search(_list, number, 0, len(_list) - 1)}')
