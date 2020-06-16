def binary_search(list_of_numbers, number_to_search):
    ascending = list_of_numbers[0] < list_of_numbers[1]
    len_of_list = len(list_of_numbers)
    first_index = 0
    last_index = len_of_list - 1
    if list_of_numbers[0] > number_to_search:
        return -1
    if list_of_numbers[len_of_list - 1] < number_to_search:
        return -1
    while first_index < last_index:
        mid_index = (first_index + last_index) // 2
        if list_of_numbers[mid_index] == number_to_search:
            return mid_index
        if list_of_numbers[mid_index] > number_to_search:
            last_index = mid_index if ascending else last_index
            first_index = mid_index if not ascending else first_index
        else:
            last_index = last_index if ascending else mid_index
            first_index = first_index if not ascending else mid_index
    return -1
