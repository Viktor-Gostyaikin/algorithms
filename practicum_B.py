'''
По трём числам определяет, выиграл игрок или нет.

Формат ввода
В первой строке записаны три случайных целых числа a, b и c.
Числа не превосходят 109 по модулю.

Формат вывода
Выведите «WIN», если игрок выиграл, и «FAIL» в противном случае.
'''

def _input(file):
    with open(file, 'r') as file:
        raw_line = file.readline().strip()
    list_of_num = list(map(int, raw_line.split()))
    return list_of_num

def game(args):
    for num in range(len(args)):
        if args[num] % 2 == 0:
            args[num] = True
        else:
            args[num] = False
    if (args[0]==args[1]) and (args[1]==args[2]):
        print('WIN')
    else: 
        print('FAIL')

args = _input('input.txt')
game(args)