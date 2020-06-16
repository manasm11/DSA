def bubble_sort(list_of_numbers):
    length_of_list = len(list_of_numbers)
    for _ in range(length_of_list - 1):
        for i in range(length_of_list - 1):
            if list_of_numbers[i] > list_of_numbers[i + 1]:
                list_of_numbers[i], list_of_numbers[i + 1] = list_of_numbers[i + 1], list_of_numbers[i]
