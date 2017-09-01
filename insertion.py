list1 = [5,7,20,1,4,2,8]

def insertion(the_list):
    n = len(the_list)
    if n == 0:
        return
    else:
        for k in range(1,n):
            tmp = the_list[k]
            i = k-1
            while i >= 0 and the_list[i] > tmp:
                the_list[i+1] = the_list[i]
                i-=1
                the_list[i+1] = tmp
    return the_list

print("Insertion: ", insertion(list1))
