def insertsort(arr):
    for i in range(1, len(arr)):
        pivot = arr[i]
        while arr[i - 1] > pivot and i > 0: # if left item larger, swap & use only positive index
            arr[i], arr[i-1] = arr[i-1], arr[i] # swap
            i = i-1 # decrement

arr = [] # empty list to append values
length = int(input('Enter length of list ')) # to determine index of loop

# append values using for-loop
for i in range(length):
    temp = int(input('Enter value '))
    arr.append(temp)

insertsort(arr)
print(arr)
