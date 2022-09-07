import random
import time
#binary-Search vs Naive search


#Regular 0(n) search method, has to iterate full list until element found
#worst case goes through full list



def naive_search(l,target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    
    return -1

#Using binary search divide and conquer
#Can leverage the fact the list is sorted 
#0(log2)

def binary_search(l,target,low=None,high=None):

    if low is None:
        low = 0

    if high is None:
        high = len(l)-1
        
    if high < low:
        return -1

    mid = (low+high)//2

    if l[mid] == target:
        return mid
    
    elif target < l[mid]:
        return binary_search(l,target,low,mid-1)
    
    else:
        return binary_search(l,target,mid+1,high)


if __name__ == '__main__':
    #l = [1,3,5,10,12]
    #target = 10
    #print(naive_search(l,target))
    #print(binary_search(l,target))

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 *length,3*length))
    
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list,target)
    end = time.time()
    print("Naive search time: ", (end-start)/length," seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list,target)
    end = time.time()
    print("Binary search time: ", (end-start)/length," seconds")
