if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        count_children = (file.readline().strip())
        children = sorted(list(map(int, file.readline().strip().split())))
        count_cookies = (file.readline().strip())
        sizes_cookies = sorted(list(map(int, file.readline().strip().split())))
    cookies = {}
    result = 0
    index = 0

    for child in children:
        while index != int(count_cookies):
            if sizes_cookies[index] >= child:
                result += 1
                index += 1
                break
            index += 1

    print(result)
