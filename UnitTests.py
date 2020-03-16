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