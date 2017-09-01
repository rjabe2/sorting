def counting_sort(string):
    count_array = [0] * 26
    sorted_array = []
    n = len(string)
    low_boundary = ord('a')

    #count each character within the string and update the count_array
    #time complexity: O(N) where N is the length of the string
    for char in string:
        position = ord(char) - low_boundary
        count_array[position] += 1

    #append all characters within the count_array that exist in the string (characters with an occurrence of at least 1)
    #time complexity: O(N*M) where N is the length of the count array, M is the most occurrences of a letter
    for i in range(len(count_array)):
        if count_array[i] > 0:
            for j in range(count_array[i]):
                sorted_array.append(chr(i + low_boundary))

    #formulate a string given the array
    #complexity: O(N)
    sort_word = ''.join(sorted_array)
    return sort_word
