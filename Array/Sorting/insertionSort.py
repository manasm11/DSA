def insertion_sort(list_of_numbers):
    length = len(list_of_numbers)
    number_at = list_of_numbers
    for current_index in range(1, length):
        current_value = number_at[current_index]
        while current_index > 0 and number_at[current_index - 1] < current_value:
            number_at[current_index] = number_at[current_index - 1]
            current_index -= 1
        number_at[current_index] = current_value
