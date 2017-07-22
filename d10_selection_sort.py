# Selection sort algorithm

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        min_value = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < min_value:
                min_value = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([5, 3, 7, 1]))  # -> [1, 3, 5, 7]
print(selection_sort([2, 7, 5, 5, 8, 1, 12, 3]))  # -> [1, 2, 3, 5, 5, 7, 8, 12]
