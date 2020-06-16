from Sorting.bubbleSort import bubble_sort
from Sorting.insertionSort import insertion_sort
from Sorting.selectionSort import selection_sort
from Sorting.quickSort import quick_sort
from Sorting.mergeSort import merge_sort
from Sorting.heapSort import heap_sort
from Sorting.utility import *


def test():
    list_of_numbers = generate_random_list(10)
    print("BEFORE SORTING:", list_of_numbers)
    start_time = timer()
    heap_sort(list_of_numbers)
    end_time = timer()
    print("AFTER SORTING:", list_of_numbers)
    print(f"SORTING TIME: {end_time - start_time} seconds.")


def compare_sorts(n):
    print("~" * 10, f"FOR {n} NUMBERS", "~" * 10)
    print("BUBBLE SORT:\t", time(bubble_sort, n))
    print("INSERTION SORT:\t", time(insertion_sort, n))
    print("SELECTION SORT:\t", time(selection_sort, n))
    print("HEAP SORT:\t", time(heap_sort, n))
    print("MERGE SORT:\t", time(merge_sort, n))
    print("QUICK SORT:\t", time(quick_sort, n))


if __name__ == '__main__':
    compare_sorts(10000)
    # test()
    # swap_vs_compare(100000000)
