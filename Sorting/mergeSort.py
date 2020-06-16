def _merge_sort(list_of_numbers):
    if len(list_of_numbers) < 2:
        return list_of_numbers
    middle_index = len(list_of_numbers) // 2
    left = _merge_sort(list_of_numbers[:middle_index])
    right = _merge_sort(list_of_numbers[middle_index:])

    i, j = 0, 0
    result = []
    while len(result) < len(left) + len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result

def merge_sort(list_of_numbers):
    list_of_numbers = _merge_sort(list_of_numbers)