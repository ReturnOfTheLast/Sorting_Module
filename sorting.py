# Importing Modules
import random

# Stalin Sort
def stalin_sort(input_list):
    i = 0
    while i < len(input_list) - 1:
        if input_list[i] > input_list[i+1]:
            del input_list[i+1]
        else: i += 1

    return input_list

# Bad Stalin Sort
def bad_stalin_sort(input_list):
    i = 0
    while i < len(input_list) - 1:
        if input_list[i] > input_list[i+1]:
            del input_list[i]
            if i > 0:
                i -= 1
        else: i += 1

    return input_list

# Bubble Sort
def bubble_sort(input_list):
    switches = 1
    while switches > 0:
        switches = 0
        for i in range(0, len(input_list) - 1):
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                switches += 1

    return input_list

# Quick Sort
def quick_sort(input_list, min_len=5):
    if len(input_list) < min_len:
        return insertion_sort(input_list)

    else:
        part = random.randint(0, len(input_list) - 1)
        split_part1 = list()
        split_part2 = list()

        for i in range(0, len(input_list)):
            if i == part:
                continue

            elif input_list[i] < input_list[part]:
                split_part1.append(input_list[i])
            else:
                split_part2.append(input_list[i])

        return_list = list()
        return_list.extend(quick_sort(split_part1, min_len))
        return_list.append(input_list[part])
        return_list.extend(quick_sort(split_part2, min_len))

    return return_list

# Bogo Sort
def bogo_sort(input_list):
    unsorted = 1
    while unsorted > 0:
        unsorted = 0
        random.shuffle(input_list)

        for i in range(0, len(input_list) - 1):
            if input_list[i] > input_list[i+1]:
                unsorted += 1

    return input_list

# Insertion Sort
def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        j = i
        for j in range(i, 0, -1):
            if not input_list[j - 1] > input_list[j]:
                break
            input_list[j], input_list[j - 1] = input_list[j - 1], input_list[j]

    return input_list
