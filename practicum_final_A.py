# 55781080
'''
    Формат ввода
    В первой строке дана длина улицы —–
    street_length (1 ≤ street_length ≤ 106).
    В следующей строке записаны street_length целых неотрицательных
    чисел — номера домов и обозначения пустых участков на карте (нули).
    Гарантируется, что в последовательности есть хотя бы один ноль.
    Номера домов (положительные числа) уникальны и не превосходят 109.

    Формат вывода
    Для каждого из участков выведите расстояние до ближайшего нуля.
    Числа выводите в одну строку, разделяя их пробелами.
'''


def calculate(street_length: int, _map: list) -> list:
    count = 0
    first_zero = False
    last_zero = None
    for index, item in enumerate(_map):
        if item == '0':
            last_zero = index
            for index_0 in range(count + 1):
                if first_zero == True:
                    if index_0 <= count / 2:
                        _map[index - index_0] = str(index_0)
                    else:
                        _map[index - index_0] = _map[index -
                                                     (count-index_0 + 1)]
                else:
                    _map[index_0] = str(count)
                    count -= 1
            if count % 2 != 0:
                ceil = int((count + 1) / 2)
                _map[index - ceil] = str(ceil)
            if not first_zero:
                first_zero = True
            count = 0
        else:
            count += 1
    for index in range(last_zero + 1, street_length):
        _map[index] = str(int(_map[index - 1]) + 1)

    return _map


def main():
    with open('input.txt', 'r') as file:
        street_length = int(file.readline().strip())
        _map = list(file.readline().strip().split())

    print(' '.join(calculate(street_length, _map)))


if __name__ == '__main__':
    main()
