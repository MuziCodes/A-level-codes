def insertsort(arr):
    for i in range(1, len(arr)):
        pointer = arr[i]
        while arr[i - 1] > pointer and i > 0: # if left item larger & positive index
            arr[i - 1], arr[i] = arr[i], arr[i - 1] # swap
            i -= 1 # decrement
    # arr[:] = arr[::-1] here for descending

# Has order of growth/time complexity as O(n²)
# Performance depends on size of array and how sorted they are.
# Especially more efficient when compared to bubble sort as
# When size is large, less swaps are made
# And when it's almost sorted, it will stop as soon as it's sorted
