def sort_hand(things_colors):
    result = []
    result_0 = []
    result_1 = []
    result_2 = []
    for el in things_colors:
        if el == '0':
            result_0.append(0)
        elif el == '1':
            result_1.append(1)
        elif el == '2':
            result_2.append(2)
    result = result_0 + result_1 + result_2
    return result


if __name__ == '__main__':
    quantity = input()
    things_colors = input().split()
    # sort_hand(things_colors)
    print(*sort_hand(things_colors))