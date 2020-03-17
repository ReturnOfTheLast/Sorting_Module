# Importing Modules
import random

# Stalin Sort
def StalinSort(args):
    i = 0
    while i < len(args) - 1:
        if args[i] > args[i+1]: del args[i+1]
        else: i += 1

    return args

# Bubble Sort
def BubbleSort(args):
    switches = 1
    while switches > 0:
        switches = 0
        for i in range(0, len(args) - 1):
            if args[i] > args[i + 1]:
                args[i], args[i + 1] = args[i + 1], args[i]
                switches += 1

    return args

# Quick Sort
def QuickSort(args, minLen):
    if len(args) < minLen:
        return(BubbleSort(args))
    else:
        part = random.randint(0, len(args) - 1)
        splitPart1 = list()
        splitPart2 = list()

        for i in range(0, len(args)):
            if i == part:
                continue
            elif args[i] < args[part]:
                splitPart1.append(args[i])
            else:
                splitPart2.append(args[i])
        
        returnList = list()
        returnList.extend(QuickSort(splitPart1, minLen))
        returnList.append(args[part])
        returnList.extend(QuickSort(splitPart2, minLen))

    return returnList

# Bogo Sort
def BogoSort(args):
    unsorted = 1
    while unsorted > 0:
        unsorted = 0
        random.shuffle(args)

        for i in range(0, len(args) - 1):
            if args[i] > args[i+1]: unsorted += 1

    return args