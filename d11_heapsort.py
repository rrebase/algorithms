# Heapsort algorithm

def build_max_heap(arr, length, i):
    l_child = 2 * i + 1
    r_child = 2 * (i + 1)
    biggest = i
    if l_child < length and arr[i] < arr[l_child]:
        biggest = l_child
    if r_child < length and arr[biggest] < arr[r_child]:
        biggest = r_child
    if biggest != i:
        arr[i], arr[biggest] = arr[biggest], arr[i]
        build_max_heap(arr, length, biggest)

def heapsort(arr):
    length = len(arr)
    start = length // 2 - 1
    for i in range(start, -1, -1):
        build_max_heap(arr, length, i)
    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        build_max_heap(arr, i, 0)
    return arr

print(heapsort([4, 10, 3, 5, 1]))  # -> [1, 3, 4, 5, 10]
print(heapsort([9, 7, 5, 5, 8, 1, 12, 14]))  # -> [1, 5, 5, 7, 8, 9, 12, 14]


# heap sort using built-in heapq library
from heapq import heappush, heappop


def heapsort2(arr):
    h = []
    [heappush(h, i) for i in arr]
    return [heappop(h) for i in range(len(h))]

print(heapsort2([4, 10, 3, 5, 1]))  # -> [1, 3, 4, 5, 10]
