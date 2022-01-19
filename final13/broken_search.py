# 59363942

def broken_search(nums, target) -> int:
    def find_pivot(low, high):
        # поиск излома
        if high < low:
            return -1
        if high == low:
            return low
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1]:
            return mid
        if mid > low and nums[mid] < nums[mid - 1]:
            return mid - 1
        if nums[low] >= nums[mid]:
            return find_pivot(low, mid - 1)
        return find_pivot(mid + 1, high)

    def binary_search(low, high):
        if high < low:
            return -1
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            return binary_search(mid + 1, high)
        return binary_search(low, mid - 1)

    high = len(nums)
    pivot = find_pivot(0, high - 1)
    if pivot == -1:
        return binary_search(0, high - 1)
    if nums[pivot] == target:
        return pivot
    if nums[0] <= target:
        return binary_search(0, pivot - 1)
    return binary_search(pivot + 1, high - 1)