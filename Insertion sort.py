def insertsort(arr):
    for i in range(1, len(arr)):
        pointer = arr[i]
        while arr[i - 1] > pointer and i > 0: # if left item larger, swap & use only positive index
            arr[i], arr[i - 1] = arr[i - 1], arr[i] # swap
            i = i - 1 # decrement
            
