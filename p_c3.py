def sort(arr1, arr2):
    index1 = 0
    index2 = 0
    while index2 != -1 and index1 != len(arr1):
        index2 = arr2.find(arr1[index1], index2)
        index1 += 1
    if index2 != -1:
        return True
    return False

def main():
    with open('input.txt', 'r') as file:
        arr1 = file.readline().strip()
        arr2 = file.readline().strip()
    print(sort(arr1, arr2))

if __name__ == '__main__':
    main()