from Array.Searching.linearSearch import linear_search
from Array.Sorting.bubbleSort import bubble_sort
from Array.Sorting.insertionSort import insertion_sort
from Array.Sorting.selectionSort import selection_sort
from Array.Sorting.quickSort import quick_sort
from Array.Sorting.mergeSort import merge_sort
from Array.Sorting.heapSort import heap_sort
from Array.utility import *


def sort_test(sort_function):
    list_of_numbers = generate_random_list(1000)
    print("BEFORE SORTING:", list_of_numbers)
    start_time = timer()
    sort_function(list_of_numbers)
    end_time = timer()
    print("AFTER SORTING:", list_of_numbers)
    print(f"SORTING TIME: {end_time - start_time} seconds.")


def sorts_compare(n):
    print("~" * 10, f"FOR {n} NUMBERS", "~" * 10)
    print("BUBBLE SORT:\t", sort_time(bubble_sort, n))
    print("INSERTION SORT:\t", sort_time(insertion_sort, n))
    print("SELECTION SORT:\t", sort_time(selection_sort, n))
    print("HEAP SORT:\t", sort_time(heap_sort, n))
    print("MERGE SORT:\t", sort_time(merge_sort, n))
    print("QUICK SORT:\t", sort_time(quick_sort, n))


def search_test(search_function):
    list_of_numbers = generate_random_list(1000)
    print("The list is:", list_of_numbers)
    number_to_search = randint(0, 10000) / 2
    start_time = timer()
    index = search_function(list_of_numbers, number_to_search)
    end_time = timer()
    print(f"{number_to_search} is at {index}")
    print(f"SEARCHING TIME: {end_time - start_time} seconds.")


def search_compare(n):
    print("~" * 10, f"FOR {n} NUMBERS", "~" * 10)
    print("LINEAR SEARCH:\t", search_time(linear_search, n), "milliseconds")
    print("BINARY SEARCH:\t", search_time(binary_search, n), "milliseconds")


if __name__ == '__main__':
    # swap_vs_compare(100000000)
    # sorts_compare(10000)
    sort_test(insertion_sort)
    # search_test(linear_search)
    # search_compare(100000)
