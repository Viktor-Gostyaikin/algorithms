'''
y = ax2 + bx + c.

Формат ввода
На вход через пробел подаются числа a, x, b, c.

Формат вывода
Выведите одно число — значение функции в точке x.
'''

def _input(file):
    with open(file, 'r') as file:
        raw_line = file.readline().strip()
    list_of_num = list(map(int, raw_line.split()))
    return list_of_num

def _calulate(args):
    '''args = [a, x, b, c].'''
    y = (args[0] * (args[1] * args[1])) + (args[2] * args[1]) + args[3]
    return y

args = _input('input.txt')
print(_calulate(args))