if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        n_and_k = list(map(int, file.readline().strip().split()))
        houses = sorted(list(map(int, file.readline().strip().split())))
    index = 0
    while index < n_and_k[0] and n_and_k[1] >= houses[index]:
        if houses[index] <= n_and_k[1]:
            n_and_k[1] -= houses[index]
        index += 1
    print(index)