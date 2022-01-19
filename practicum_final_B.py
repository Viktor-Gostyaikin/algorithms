# 55780232
'''
Формат ввода
В первой строке дано целое число k (1 ≤ k ≤ 5).

В четырёх следующих строках задан вид тренажёра –— по 4 символа
в каждой строке. Каждый символ —– либо точка, либо цифра от 1 до 9.
Символы одной строки идут подряд и не разделены пробелами.

Формат вывода
Выведите единственное число –— максимальное количество баллов,
которое смогут набрать Гоша и Тимофей.
'''

def calculate(game_keys: int, key_values: str) -> str:
    score = 0
    num = {
        '1': 0, '2': 0, '3': 0, '4': 0,
        '5': 0, '6': 0, '7': 0, '8': 0, '9': 0
    }
    for value in key_values:
        if value in num.keys():
            num[value] += 1
    for time in range(1, 10):
        if 0 < num[str(time)] <= game_keys:
            score += 1
    return score


def main():
    with open('input.txt', 'r') as file:
        game_keys = (int(file.readline().strip())) * 2
        key_values = ''
        for index in range(4):
            key_values += file.readline().strip()

    print(calculate(game_keys, key_values))


if __name__ == '__main__':
    main()
