# Quicksort algorithm


def quicksort(array):
    less, equal, greater = [], [], []

    if len(array) <= 1:  # recursive base
        return array

    pivot = array[0]

    for element in array:
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)

    return quicksort(less) + equal + quicksort(greater)  # concatenate lists


print(quicksort([9, 7, 5, 5, 8, 1, 12, 14]))  # -> [1, 5, 5, 7, 8, 9, 12, 14]
print(quicksort([44, 46, 1, 46, 13, 61, 46, 48, 81, 46, 91, 1, 99, 98, 60, 10, 8, 37, 22, 91]))
# -> [1, 1, 8, 10, 13, 22, 37, 44, 46, 46, 46, 46, 48, 60, 61, 81, 91, 91, 98, 99]
