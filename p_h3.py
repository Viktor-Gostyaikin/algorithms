def sort(n, arr):
    changed = True
    GAP = 1
    while changed:
        changed = False
        for item in range(n - 1):
            if arr[item] + arr[item+GAP] < arr[item+GAP] + arr[item]:
                arr[item], arr[item+GAP] = arr[item+GAP], arr[item]
                changed = True
    return arr

def main():
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        arr = file.readline().strip().split()
    print(''.join(sort(n, arr)))
        

if __name__ == '__main__':
    main()