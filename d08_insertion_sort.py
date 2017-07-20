# Insertion sort algorithm

def insertion_sort(arr):
    for i in range(1, len(arr)):
        pivot = arr[i]
        j = i - 1
        # move element at pivot left until it's the first element or in sorted position
        while j >= 0 and pivot < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = pivot  # put element at pivot into new position
    return arr

print(insertion_sort([5, 3, 7, 1]))  # -> [1, 3, 5, 7]
print(insertion_sort([2, 7, 5, 5, 8, 1, 12, 3]))  # -> [1, 2, 3, 5, 5, 7, 8, 12]
