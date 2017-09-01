def binarySearch(list,key):
    if len(list) <=  0:
        return "ERROR"
    low = 0
    high = len(list)

    found = False
    while (low <= high-1) and not found:
        mid = (low+high)//2
        if (key == list[mid]):
            found = True
        else:
            if key < list[mid]:
                high = mid-1
            else:
                low = mid + 1
            return found
list1 = [5,7,20,1,4,2,8]
print(binarySearch(list1,20))       
