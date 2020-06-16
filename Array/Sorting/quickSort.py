def _quick_sort(list_of_numbers, low_index, high_index):
    arr = list_of_numbers
    if low_index < high_index:
        i = low_index - 1
        pivot = arr[high_index]
        for j in range(low_index, high_index):
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high_index] = arr[high_index], arr[i + 1]
        pivot_index = i + 1
        _quick_sort(arr, low_index, pivot_index - 1)
        _quick_sort(arr, pivot_index + 1, high_index)


def quick_sort(list_of_numbers):
    _quick_sort(list_of_numbers, 0, len(list_of_numbers) - 1)
