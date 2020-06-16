def _heapify(arr, n, i):
    minimum = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] > arr[left]:
        minimum = left
    if right < n and arr[minimum] > arr[right]:
        minimum = right
    if minimum != i:
        arr[i], arr[minimum] = arr[minimum], arr[i]
        _heapify(arr, n, minimum)


def heap_sort(list_of_numbers):
    n = len(list_of_numbers)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(list_of_numbers, n, i)
    arr = list_of_numbers
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)
