abc = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],#
    '6': ['m', 'n', 'o'],#
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],#
    '9': ['w', 'x', 'y', 'z'],#
}

def product(*args):
    pools = [pool for pool in args]
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        if len(prod) == len(args):
            yield ''.join(prod)

def main():
    with open('input.txt', 'r') as file:
        buttons = list(file.readline().strip())
    pressd_buttons = []
    for button in buttons:
        pressd_buttons.append(abc[button])

    print(*product(*pressd_buttons), sep=' ')

if __name__ == '__main__':
    main()