# Dynamic programming - longest increasing subsequence
# TODO: O(nlogn) solution


def lis(arr):
    """
    Return the longest increasing subsequence of an array.
    O(n^2)
    """
    lengths = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                lengths[i] = max(lengths[i], lengths[j] + 1)

    max_value = max(lengths)
    result = []
    for v in range(len(lengths) - 1, -1, -1):
        if max_value == lengths[v]:
            result.append(arr[v])
            max_value -= 1

    return result[::-1]


print(lis([4, 1, 2, 6, 1, 7, 3, 8, 5]))  # -> [1, 2, 6, 7, 8]
