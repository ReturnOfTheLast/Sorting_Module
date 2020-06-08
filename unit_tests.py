# Import module
import sorting

# Stalin Sort tests
STALIN_COUNT = 3
STALIN_SUCCESS = 0

if sorting.stalin_sort([5, 3, 55, 7, 9, 3, 2, 5, 2]) == [5, 55]:
    STALIN_SUCCESS += 1

if sorting.stalin_sort([6, 3, 22, 432, 666, 44, 9]) == [6, 22, 432, 666]:
    STALIN_SUCCESS += 1

if sorting.stalin_sort([8, 4, 22, 134, 88, 3, 999, 332, 445]) == [8, 22, 134, 999]:
    STALIN_SUCCESS += 1

print("Stalin Sort: " + str(STALIN_SUCCESS) + "/" + str(STALIN_COUNT))

# Stalin Sort tests
BAD_STALIN_COUNT = 3
BAD_STALIN_SUCCESS = 0

if sorting.bad_stalin_sort([5, 3, 55, 7, 9, 3, 2, 5, 2]) == [2, 2]:
    BAD_STALIN_SUCCESS += 1

if sorting.bad_stalin_sort([6, 3, 22, 432, 666, 44, 9]) == [3, 9]:
    BAD_STALIN_SUCCESS += 1

if sorting.bad_stalin_sort([8, 4, 22, 134, 88, 3, 999, 332, 445]) == [3, 332, 445]:
    BAD_STALIN_SUCCESS += 1

print("Bad Stalin Sort: " + str(BAD_STALIN_SUCCESS) + "/" + str(BAD_STALIN_COUNT))

# Bubble Sort tests
BUBBLE_COUNT = 3
BUBBLE_SUCCESS = 0

if sorting.bubble_sort([6, 4, 2, 11, 443, 554, 66]) == [2, 4, 6, 11, 66, 443, 554]:
    BUBBLE_SUCCESS += 1

if sorting.bubble_sort([7, 9, 3, 5, 23, 55, 34, 6]) == [3, 5, 6, 7, 9, 23, 34, 55]:
    BUBBLE_SUCCESS += 1

if sorting.bubble_sort([8, 3, 234, 554, 555, 6663, 2]) == [2, 3, 8, 234, 554, 555, 6663]:
    BUBBLE_SUCCESS += 1

print("Bubble Sort: " + str(BUBBLE_SUCCESS) + "/" + str(BUBBLE_COUNT))

# Quick Sort tests
QUICK_COUNT = 3
QUICK_SUCCESS = 0
MIN_LEN = 1

if sorting.quick_sort([23, 55, 4, 33, 2, 66, 4], MIN_LEN) == [2, 4, 4, 23, 33, 55, 66]:
    QUICK_SUCCESS += 1

if sorting.quick_sort([5, 32, 55, 12, 44, 33, 86], MIN_LEN) == [5, 12, 32, 33, 44, 55, 86]:
    QUICK_SUCCESS += 1

if sorting.quick_sort([9, 3, 45, 23, 55, 432, 55], MIN_LEN) == [3, 9, 23, 45, 55, 55, 432]:
    QUICK_SUCCESS += 1

print("Quick Sort: " + str(QUICK_SUCCESS) + "/" + str(QUICK_COUNT))

# Bogo Sort tests
BOGO_COUNT = 3
BOGO_SUCCESS = 0

if sorting.bogo_sort([6, 8, 2, 13, 55, 332, 4]) == [2, 4, 6, 8, 13, 55, 332]:
    BOGO_SUCCESS += 1

if sorting.bogo_sort([6, 3, 2, 4, 932, 44, 32]) == [2, 3, 4, 6, 32, 44, 932]:
    BOGO_SUCCESS += 1

if sorting.bogo_sort([6, 5, 6, 33, 63, 33, 6, 44]) == [5, 6, 6, 6, 33, 33, 44, 63]:
    BOGO_SUCCESS += 1

print("Bogo Sort: " + str(BOGO_SUCCESS) + "/" + str(BOGO_COUNT))

# Insertion Sort tests
INSERTION_COUNT = 3
INSERTION_SUCCESS = 0

if sorting.insertion_sort([6, 3, 23, 55, 33, 2, 54]) == [2, 3, 6, 23, 33, 54, 55]:
    INSERTION_SUCCESS += 1

if sorting.insertion_sort([7, 32, 44, 554, 32, 6, 3]) == [3, 6, 7, 32, 32, 44, 554]:
    INSERTION_SUCCESS += 1

if sorting.insertion_sort([3, 53, 23, 5, 77, 54, 83]) == [3, 5, 23, 53, 54, 77, 83]:
    INSERTION_SUCCESS += 1

print("Insertion Sort: " + str(INSERTION_SUCCESS) + "/" + str(INSERTION_COUNT))
