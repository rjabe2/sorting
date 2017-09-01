def quick_select(array, k):
    if len(array) != 0:
        pivot = array[(len(array) // 2)]
    smallerList = []
    for i in array:
        if i < pivot:
            smallerList.append(i)
    largerList = []
    for i in array:
        if i > pivot:
            largerList.append(i)

    count = len(array) - len(smallerList) - len(largerList)
    n = len(smallerList)
    if k >= n and k < (n+count):
        return pivot
    elif n > k:
        return quick_select(smallerList, k)
    else:
        return quick_select(largerList, k-n-count)
