# Binary search algorithm


def binary_search(array, item):
    lower, upper = 0, len(array)
    while lower < upper:
        mid = (lower + upper) // 2  # middle
        if array[mid] < item:
            lower = mid + 1
        elif array[mid] > item:
            upper = mid
        else:
            return mid
    return False


l = [9, 21, 25, 26, 30, 35, 38, 63, 64, 65, 69, 70, 71, 77, 78, 80, 89]
print(binary_search(l, 25))  # -> 2
