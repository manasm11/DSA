from random import randint
from timeit import default_timer as timer
from Array.Sorting.quickSort import quick_sort
from Array.Searching.binarySearch import binary_search


def swap_vs_compare(n=10000):
    start = timer()
    for i in range(n):
        temp = 23 >= 34
    end = timer()
    print(f"Time for {n} comparisons = {end - start}")
    temp = 1
    temp2 = 23
    start = timer()
    for i in range(n):
        temp, temp2 = temp2, temp
    end = timer()
    print(f"Time for {n} swaps = {end - start}")


def sort_time(function, n=1000):
    list_of_numbers = generate_random_list(n)
    start = timer()
    function(list_of_numbers)
    end = timer()
    return end - start


def search_time(function, n=1000):
    list_of_numbers = generate_random_list(n)
    if function == binary_search:
        quick_sort(list_of_numbers)
    start = timer()
    function(list_of_numbers, 1000.0)
    end = timer()
    return (end - start) * 1000


def input_list_from_user():
    list_of_numbers = list()
    current_input = 1
    while True:
        current_input = input("Enter number (n to exit) >> ")
        if current_input == 'n':
            return list_of_numbers
        try:
            list_of_numbers.append(float(current_input))
        except TypeError:
            print("[-] Invelid input !!! (n to exit)")
        except ValueError:
            print("[-] Please enter some number. (n to exit)")


def input_list_from_file(filename):
    list_of_numbers = list()
    try:
        with open(filename, "r") as file:
            for number in map(float, file.read().strip().split()):
                list_of_numbers.append(number)
    except FileNotFoundError:
        print("[-] FILE NOT FOUND !!!")
        exit(-1)
    except TypeError:
        print("[-] File contains some non numeric values !!!")
        exit(-2)
    return list_of_numbers


def generate_random_list_to_file(n=None):
    if not n:
        n = input("ENTER NUMBER OF NUMBERS TO BE GENERATED >> ")
    try:
        n = int(n)
    except ValueError:
        print("generate_list_to_file: BHAI INTEGER DAAL DO PLEASE !!!")
    with open(f"{n}_numbers", "w") as ouput_file:
        for _ in range(n):
            ouput_file.write(f"{randint(-10000, 10000) / 2} ")


def generate_random_list(n=None):
    list_of_numbers = list()
    if not n:
        n = input("ENTER NUMBER OF NUMBERS TO BE GENERATED >> ")
    try:
        n = int(n)
    except ValueError:
        print("generate_list: BHAI INTEGER DAAL DO PLEASE !!!")
    for _ in range(n):
        list_of_numbers.append(randint(-10000, 10000) / 2)
    return list_of_numbers


def test():
    print(generate_random_list(10))
