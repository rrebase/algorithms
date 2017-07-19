# Merge sort algorithm


def merge_sort(arr):
    result = []
    if len(arr) <= 1:
        return arr
    middle = int(len(arr) / 2)
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:] + right[j:]
    return result


print(merge_sort([2, 1, 7, 3, 5, 2, 12, 2, 8, 0, 13]))  # -> [0, 1, 2, 2, 2, 3, 5, 7, 8, 12, 13]
