# Name: Calder Prulhiere
# OSU Email: prulhiec@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 1
# Due Date: 7/11/2023
# Description: A python file containing my answers to assignment 1, consists of 10 pythons functions implemented with
# O(N) complexity


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple[int, int]:
    """
    sorts through an array and returns the min and max elements in a tuple
    """
    min_val = arr[0]
    max_val = arr[0]

    for i in range(arr.length()):

        if arr[i] < min_val:
            min_val = arr[i]

        if arr[i] > max_val:
            max_val = arr[i]

    return (min_val, max_val)


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

#
def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Takes an array of integers, checks if the values are divisable by 3, 5 or both and based on that operation assigns
    a word to them in a new array
    """
    length = arr.length()
    new_arr = StaticArray(length)

    for i in range(length):
        number = arr.get(i)

        if number % 3 == 0 and number % 5 == 0:
            new_arr.set(i, 'fizzbuzz')

        elif number % 3 == 0:
            new_arr.set(i, 'fizz')

        elif number % 5 == 0:
            new_arr.set(i, 'buzz')

        else:
            new_arr.set(i, number)

    return new_arr


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    Reverses the order of the elements in the input array in place.
    """

    length = arr.length()

    for i in range(length // 2):
        val = arr.get(i)
        arr.set(i, arr.get(length - i - 1))
        arr.set(length - i - 1, val)


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    creates a new array simliar to the original, shifting their positions based on the values of steps, if
    steps is a positive integer elements aree shifted right, negative integer elements shifted left
    """

    length = arr.length()
    new_arr = StaticArray(length)

    for i in range(length):
        new_position = (i + steps) % length
        new_arr[new_position] = arr[i]

    return new_arr
# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    Returns an array with the orignal values of start and end, while including all the values the between the two
    """

    # using abs to determine the size of the arr
    size = abs(end - start) + 1
    arr = StaticArray(size)
    if start <= end:
        for i in range(size):
            arr[i] = start + i
    else:
        for i in range(size):
            arr[i] = start - i
    return arr

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    Returns 1 if the array is in ascending order, -1 if the array is in descending order, and 0 otherwise.
    """
    # Initial array check
    if arr.length() <= 1:
        return 1

    # comparing size of elements, determining direction
    if arr[0] < arr[1]:
        order = 1 #ascend
    elif arr[0] > arr[1]:
        order = -1 #decend
    else:
        return 0  # neither

    # after determining direction start check at third element
    for i in range(2, arr.length()):
        if (order == 1 and arr[i] <= arr[i - 1]) or \
           (order == -1 and arr[i] >= arr[i - 1]):
            return 0  # array is not sorted in the expected order

    return order

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    Returns a tuple containing the mode of an array and how many times it appears
    """

    value = arr[0]
    freq = 1

    max_value = value
    max_freq = freq

    for i in range(1, arr.length()):
        # Check current and previous
        if arr[i] == value:
            freq += 1
        else:
            # reset
            value = arr[i]
            freq = 1

        if freq > max_freq:
            max_value = value
            max_freq = freq

    return (max_value, max_freq)

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Returns original array free of any duplicate values
    """
    temp = StaticArray(arr.length())
    unique_count = 0

    for i in range(arr.length()):

        if i == 0 or arr[i] != arr[i - 1]:
            temp[unique_count] = arr[i]
            unique_count += 1

    # new array, number of unique elements
    result = StaticArray(unique_count)
    for i in range(unique_count):
        result[i] = temp[i]


    return result

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:

   pass


# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    Takes an array of integers, squares each element and returns the squared values in a new array,
    sorted in ascending order.
    """
    result = StaticArray(arr.length())

    # Initialize two pointers start and end
    left, right = 0, arr.length() - 1

    # populate array from end to start
    for i in range(arr.length() - 1, -1, -1):
        if abs(arr[left]) >= abs(arr[right]):
            result[i] = arr[left] ** 2
            left += 1
        else:
            result[i] = arr[right] ** 2
            right -= 1

    return result


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
