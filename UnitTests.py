# Import module
import Sorting

# Stalin Sort tests
stalinCount = 3
stalinSuccess = 0

if Sorting.StalinSort([5, 3, 55, 7, 9, 3, 2, 5, 2]) == [5, 55]:
    stalinSuccess += 1

if Sorting.StalinSort([6, 3, 22, 432, 666, 44, 9]) == [6, 22, 432, 666]:
    stalinSuccess += 1

if Sorting.StalinSort([8, 4, 22, 134, 88, 3, 999, 332, 445]) == [8, 22, 134, 999]:
    stalinSuccess += 1

print("Stalin Sort: " + str(stalinSuccess) + "/" + str(stalinCount))

# Bubble Sort tests
bubbleCount = 3
bubbleSuccess = 0

if Sorting.BubbleSort([6, 4, 2, 11, 443, 554, 66]) == [2, 4, 6, 11, 66, 443, 554]:
    bubbleSuccess += 1

if Sorting.BubbleSort([7, 9, 3, 5, 23, 55, 34, 6]) == [3, 5, 6, 7, 9, 23, 34, 55]:
    bubbleSuccess += 1

if Sorting.BubbleSort([8, 3, 234, 554, 555, 6663, 2]) == [2, 3, 8, 234, 554, 555, 6663]:
    bubbleSuccess += 1

print("Bubble Sort: " + str(bubbleSuccess) + "/" + str(bubbleCount))

# Quick Sort tests
quickCount = 3
quickSuccess = 0
minLen = 1

if Sorting.QuickSort([23, 55, 4, 33, 2, 66, 4], minLen) == [2, 4, 4, 23, 33, 55, 66]:
    quickSuccess += 1

if Sorting.QuickSort([5, 32, 55, 12, 44, 33, 86], minLen) == [5, 12, 32, 33, 44, 55, 86]:
    quickSuccess += 1

if Sorting.QuickSort([9, 3, 45, 23, 55, 432, 55], minLen) == [3, 9, 23, 45, 55, 55, 432]:
    quickSuccess += 1

print("Quick Sort: " + str(quickSuccess) + "/" + str(quickCount))

# Bogo Sort tests
bogoCount = 3
bogoSuccess = 0

if Sorting.BogoSort([6, 8, 2, 13, 55, 332, 4]) == [2, 4, 6, 8, 13, 55, 332]:
    bogoSuccess += 1

if Sorting.BogoSort([6, 3, 2, 4, 932, 44, 32]) == [2, 3, 4, 6, 32, 44, 932]:
    bogoSuccess += 1

if Sorting.BogoSort([6, 5, 6, 33, 63, 33, 6, 44]) == [5, 6, 6, 6, 33, 33, 44, 63]:
    bogoSuccess += 1

print("Bogo Sort: " + str(bogoSuccess) + "/" + str(bogoCount))

# Insertion Sort tests
insertionCount = 3
insertionSuccess = 0

if Sorting.InsertionSort([6, 3, 23, 55, 33, 2, 54]) == [2, 3, 6, 23, 33, 54, 55]:
    insertionSuccess += 1

if Sorting.InsertionSort([7, 32, 44, 554, 32, 6, 3]) == [3, 6, 7, 32, 32, 44, 554]:
    insertionSuccess += 1

if Sorting.InsertionSort([3, 53, 23, 5, 77, 54, 83]) == [3, 5, 23, 53, 54, 77, 83]:
    insertionSuccess += 1

print("Insertion Sort: " + str(insertionSuccess) + "/" + str(insertionCount))