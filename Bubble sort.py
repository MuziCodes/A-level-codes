def bubsort(arr):
    for i in range(len(arr)-1):  # 2nd last element so -1
        for j in range(len(arr)-i-1):  # ignore sorted so -i-1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
    # arr[:] = arr[::-1] here for descending order

# Has order of growth/time complexity as O(n²) but O(n) if list already sorted
# Goes through all elements and swaps by comparing with next value for each pass
