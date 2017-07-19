# Bubble sort algorithm


def bubble_sort(arr):
    while True:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]  # swap
                swapped = True
        if not swapped:
            break
    return arr


print(bubble_sort([15, 14, 10, 17, 10, 9, 7, 14, 16, 11, 9, 9, 6, 13, 12]))  # -> [6, 7, 9, 9, 9, 10, 10, 11, 12, 13, 14, 14, 15, 16, 17]
