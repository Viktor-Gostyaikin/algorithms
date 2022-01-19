'''
Формат ввода
    В первой строке задано количество садовников n. Число садовников не
    превосходит 100 000. В следующих n строках через пробел записаны
    координаты клумб в формате: start end, где start —– координата начала,
    end —– координата конца. Оба числа целые, неотрицательные и не 
    превосходят 107. start строго меньше, чем end.

Формат вывода
    Нужно вывести координаты каждой из получившихся клумб в отдельных 
    строках. Данные должны выводится в отсортированном порядке —– сначала
    клумбы с меньшими координатами, затем —– с бОльшими.
'''

def calculate(flowers):
    result = []
    result.append(flowers[0])
    for flower in flowers[1::]:
        append_box = True
        if result[-1][0] <= flower[0] <= result[-1][1] and flower[1] > result[-1][1]:
            result[-1][1] = flower[1]
            append_box = False
            pass
        elif flower[0] <= result[-1][0] or flower[1] <= result[-1][1]:
            append_box = False
            pass
        if append_box:
            result.append(flower)
    return result

def main():
    with open('input.txt', 'r') as file:
        gardnr = int(file.readline().strip())
        flowers = [list(map(int, file.readline().strip().split())) for idx in range(gardnr)]
    flowers = sorted(flowers)
    for flow in calculate(flowers):
        print(*flow)

if __name__ == '__main__':
    main()