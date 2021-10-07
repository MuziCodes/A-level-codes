def bubsort(arr):
    for i in range(len(arr)-1, 0, -1): # loop from length to 0 (reverse)
        for j in range(i): # again loop for multiple passes
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swap
  # arr[::-1] here for descending order

arr = [] # empty list to append values
length = int(input('Enter length of list ')) # to determine index of loop

# append values using for-loop
for i in range(length):
    temp = int(input('Enter value '))
    arr.append(temp)

bubsort(arr)
print(arr)
