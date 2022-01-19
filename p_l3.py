# def sort(days, arr, price):
#     first = -1
#     second = -1
#     for day, val in enumerate(arr):
#         if first == -1 and val >= price:
#             first = day + 1
#         if second == -1 and val >= price * 2:
#             second = day + 1
#             break
#     return first, second

def sort(arr, price, left=0, right=0):
    mid = 1
    if arr[left] >= price:
        return left + 1
    while (left <= right) and mid != 0:
            mid = (left + right) // 2
            if arr[mid - 1] < price <= arr[mid]:
                return mid + 1
            elif price <= arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1

def main():
    with open('input.txt', 'r') as file:
        days = int(file.readline().strip()) - 1
        arr = list(map(int, file.readline().strip().split()))
        price = int(file.readline().strip())
    first = sort(arr, price, left=0, right=days)
    if first == -1:
        second = -1
    else:
        second = sort(arr, price*2, left=first, right=days)
    print(first, second)

if __name__ == '__main__':
    main()