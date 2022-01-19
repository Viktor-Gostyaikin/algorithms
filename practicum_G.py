'''
    Формат ввода
    На вход подаётся целое число в диапазоне от 0 до 10000.

    Формат вывода
    Выведите двоичное представление этого числа.
'''
def _input(file):
    with open(file, 'r') as file:
        _dec = int(file.readline().strip())
    return _dec

def calculate(_dec, _bin=''):
    while _dec != 0:
        _bin += str(_dec%2)
        _dec = _dec // 2

    return _bin[::-1]


print(calculate(_input('input.txt')))