def insertsort(arr):
    for i in range(1, len(arr)):
        pointer = arr[i]
        while arr[i - 1] > pointer and i > 0: # if left item larger & positive index
            arr[i - 1], arr[i] = arr[i], arr[i - 1] # swap
            i -= 1 # decrement
    # arr[:] = arr[::-1] here for descending
