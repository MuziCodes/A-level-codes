def bubsort(arr):
    for i in range(len(arr)-1): # 2nd last element so -1
        for j in range(len(arr)-i-1): # again loop for multiple passes
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swap
  # arr[::-1] here for descending order
