def bubsort(arr):
    for i in range(len(arr)-1, 0, -1): # reverse order, length to 0
        for j in range(i): # again loop for multiple passes
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swap
  # arr[::-1] here for descending order

array = [] # empty list to append values
length = int(input('Enter length of list ')) # to determine index of loop

# append values using for-loop
for i in range(length):
    temp = input('Enter value ')
    array.append(temp)

bubsort(array)
