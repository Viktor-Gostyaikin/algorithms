'''
    Формат ввода
    В первой строке — длина списочной формы числа X. На следующей строке — сама списочная форма с цифрами записанными через пробел.

    В последней строке записано число K.

    Формат вывода
    Выведите списочную форму числа X+K.
'''
def _input(file):
    with open(file, 'r') as file:
        length = int(file.readline().strip())
        a = int(''.join(file.readline().strip().split())[:length])
        b = int(file.readline().strip())
    return a, b
def calculate(a, b):
    a += b
    a = str(a)
    b = ' '.join(a)
    return(b)
print(calculate(*_input('input.txt')))