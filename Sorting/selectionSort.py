def selection_sort(list_of_numbers):
    length = len(list_of_numbers)
    for i in range(length):
        max_index = i
        for j in range(i, length):
            max_index = j if list_of_numbers[j] > list_of_numbers[max_index] else max_index
        list_of_numbers[i], list_of_numbers[max_index] = list_of_numbers[max_index], list_of_numbers[i]
