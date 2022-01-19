'''
Формат ввода
В первой строке задано число n — количество строк матрицы.
Во второй строке задано m — число столбцов, m и n не превосходят 1000.
В следующих n строках задана матрица. Числа в ней не превосходят по модулю 1000.

Формат вывода
Напечатайте транспонированную матрицу в том же формате,
который задан во входных данных. Каждая строка матрицы 
выводится на отдельной строке,
элементы разделяются пробелами.
'''
def calculate(matrix: list, lines: int, columns:int) -> str:
    retranslator = []
    for index in range(columns):
        retranslator.append([matrix[0][index]])
    for index_1 in range(columns):
        for index_2 in range(1, lines):
            retranslator[index_1].append(matrix[index_2][index_1])
    result = ''
    for line in retranslator:
        result += ' '.join(line) + '\n'
    return result

def main():
    matrix = []
    with open('input.txt', 'r') as file:
        lines = int(file.readline().strip())
        columns = int(file.readline().strip())
        for index in range(lines):
            matrix.append(list(file.readline().strip().split()))

    print(calculate(matrix, lines, columns))

if __name__ == '__main__':
    main()