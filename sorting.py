# Importing Modules
import random

# Stalin Sort
def stalin_sort(args):
    i = 0
    while i < len(args) - 1:
        if args[i] > args[i+1]:
            del args[i+1]
        else: i += 1

    return args

# Bad Stalin Sort
def bad_stalin_sort(args):
    i = 0
    while i < len(args) - 1:
        if args[i] > args[i+1]:
            del args[i]
            if i > 0:
                i -= 1
        else: i += 1

    return args

# Bubble Sort
def bubble_sort(args):
    switches = 1
    while switches > 0:
        switches = 0
        for i in range(0, len(args) - 1):
            if args[i] > args[i + 1]:
                args[i], args[i + 1] = args[i + 1], args[i]
                switches += 1

    return args

# Quick Sort
def quick_sort(args, min_len):
    if len(args) < min_len:
        return bubble_sort(args)

    else:
        part = random.randint(0, len(args) - 1)
        split_part1 = list()
        split_part2 = list()

        for i in range(0, len(args)):
            if i == part:
                continue

            elif args[i] < args[part]:
                split_part1.append(args[i])
            else:
                split_part2.append(args[i])

        return_list = list()
        return_list.extend(quick_sort(split_part1, min_len))
        return_list.append(args[part])
        return_list.extend(quick_sort(split_part2, min_len))

    return return_list

# Bogo Sort
def bogo_sort(args):
    unsorted = 1
    while unsorted > 0:
        unsorted = 0
        random.shuffle(args)

        for i in range(0, len(args) - 1):
            if args[i] > args[i+1]:
                unsorted += 1

    return args

# Insertion Sort
def insertion_sort(args):
    for i in range(1, len(args)):
        j = i
        for j in range(i, 0, -1):
            if not args[j - 1] > args[j]:
                break
            args[j], args[j - 1] = args[j - 1], args[j]

    return args
