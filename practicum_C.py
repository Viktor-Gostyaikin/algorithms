'''
Функция, которая для элемента матрицы возвращает всех его соседей.
Формат ввода
В первой строке задано n — количество строк матрицы. Во второй — количество столбцов m. Числа m и n не превосходят 1000. В следующих n строках задана матрица. Элементы матрицы — целые числа, по модулю не превосходящие 1000. В последних двух строках записаны координаты элемента (индексация начинается с нуля), соседей которого нужно найти.

Формат вывода
Напечатайте нужные числа в возрастающем порядке через пробел.'''
def _input(file):
    matrix = []
    with open(file, 'r') as file:
        lines_mtrx = int(file.readline().strip())
        column_mtrx = int(file.readline().strip())
        for line in range(lines_mtrx):
            matrix.append(list(map(int, file.readline().strip().split())))
        line = int(file.readline().strip())
        colomn = int(file.readline().strip())
    return matrix, lines_mtrx, column_mtrx, line, colomn

def calculate(matrix, lines_mtrx, column_mtrx, line, colomn):
    result = []
    try:
        if line - 1 >= 0:
            result.append(matrix[line-1][colomn])
    except:
        pass
    try:
        if colomn - 1 >= 0:
            result.append(matrix[line][colomn-1])
    except:
        pass
    try:
        result.append(matrix[line+1][colomn])
    except:
        pass
    try:
        result.append(matrix[line][colomn+1])
    except:
        pass
    return sorted(result)


print(' '.join(map(str, calculate(*_input('input.txt')))))