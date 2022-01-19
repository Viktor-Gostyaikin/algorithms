'''
Формат ввода
На вход подаётся целое число в диапазоне от 1 до 10000.

Формат вывода
Выведите «True», если число является степенью четырёх, «False» –— в обратном случае.
'''
import math
def _input(file):
    with open(file, 'r') as file:
        num = int(file.readline().strip())
    return num

def calculate(num):
    if math.log(num, 4).is_integer():
        return True
    return False

print(calculate(_input('input.txt')))