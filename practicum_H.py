'''
    Формат ввода
    Два числа в двоичной системе счисления, каждое на отдельной строке.
    Длина каждого числа не превосходит 10 000 символов.

    Формат вывода
    Одно число в двоичной системе счисления.
'''
def _input(file):
    with open(file, 'r') as file:
        a = list(map(int, list(file.readline().strip())))
        b = list(map(int, list(file.readline().strip())))
    return a, b

def _calculate(a, b):
    if len(b) > len(a):
        a, b = b, a
    for i in range(len(b)):
        if a[-i-1] + b[-i-1] == 0:
            pass
        elif a[-i-1] + b[-i-1] == 1:
            a[-i-1] = 1
        elif a[-i-1] + b[-i-1] == 2:
            a[-i-1] = 0
            try:
                a[-i-2] += 1
            except:
                a = [1,] + a
        elif a[-i-1] + b[-i-1] == 3:
            a[-i-1] = 1
            try:
                a[-i-2] += 1
            except:
                a = [1,] + a
    for i in range(len(a)+1):
        if a[-i] == 2:
            a[-i] = 0
            try:
                a[-i-1] += 1
            except:
                a = [1,] + a
    return ''.join(map(str, a))

print(_calculate(*_input('input.txt')))