'''
    Назовём хаотичностью погоды за n дней количество дней,
    в которые температура строго больше, чем в день до (если такой существует) и
    в день после текущего (если такой существует).

    Формат ввода
    В первой строке дано число n –— длина периода измерений в днях, 1 ≤ n≤ 105.
    Во второй строке даны n целых чисел –— значения температуры в каждый из n дней.
    Значения температуры не превосходят 273 по модулю.

    Формат вывода
    Выведите единственное число — хаотичность за данный период.
'''
def _input(file):
    with open(file, 'r') as file:
        days = int(file.readline().strip())
        t = file.readline().strip()
    list_of_t = list(map(int, t.split()))
    return days, list_of_t

def _calculate(days:int, list_of_t:list, chaos=0):
    if len(list_of_t) == 1:
        return 1
    else:
        if list_of_t[0] > list_of_t[1]:
            chaos += 1
        if list_of_t[-1] > list_of_t[-2]:
            chaos += 1
        for i in range(1, days-1):
            if list_of_t[i] > list_of_t[i-1] and list_of_t[i] > list_of_t[i+1]:
                chaos += 1
    return chaos

print(_calculate(*_input('input.txt')))