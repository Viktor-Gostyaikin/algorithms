'''
    Формат ввода
    На вход подаются строки s и t, разделенные переносом строки. Длины строк не превосходят 1000 символов. Строки не бывают пустыми.

    Формат вывода
    Выведите лишнюю букву.
'''
def _input(file):
    with open(file, 'r') as file:
        s = file.readline().strip()
        t = file.readline().strip()
    return s, t

def calculate(s, t):
    for l in s:
        t = t.replace(l, '', 1)
    return t

print(calculate(*_input('input.txt')))
