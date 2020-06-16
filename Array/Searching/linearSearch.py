def linear_search(list_of_numbers, number_to_search):
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] == number_to_search:
            return i
    return -1
