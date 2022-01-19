def sort(n, arr):
    changed = True
    GAP = 1
    result = []
    while changed:
        changed = False
        for item in range(n - 1):
            if arr[item] > arr[item+GAP]:
                arr[item], arr[item+GAP] = arr[item+GAP], arr[item]
                changed = True
        if changed:
            result.append(arr.copy())
    if result:
        return result
    return [arr]


def main():
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))
    for idx in sort(n, arr):
        print(*idx)

if __name__ == '__main__':
    main()