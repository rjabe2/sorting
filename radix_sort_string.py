def radix(array, i):
    #recursively sort an array using radix sort
    #time complexity: O(N*M) where N is number of strings in array, M is length of each string
    #worst case time complexity: O(N+M) where N is # of strings, M is length of string
    finished = []
    low_boundary = ord('a')

    if len(array) <= 1:
        return array

    #creates a bucket for each letter
    bucket = [[] for x in range(27)]

    for string in array:
        if i >= len(string):
            finished.append(string)
        else:
            bucket[ord(string[i])-low_boundary].append(string)

    bucket = [radix(letter, i+1) for letter in bucket]

    words = []
    for bucketlist in bucket:
        for b in bucketlist:
            words.append(b)

    complete_set = finished + words

    return complete_set
    
list = ["palped","dapple","lapper","lappet","rappel","papule","appeal"] #test radix sort on unsorted list
print(radix(list,0))
