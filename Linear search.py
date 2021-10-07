def linsearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print('Found at position', i + 1)
            break
    else:
        print('Not found')

arr = [] # empty list to append values
length = int(input('Enter length of list ')) # to determine index of loop

# append values using for-loop
for i in range(length):
    temp = int(input('Enter value '))
    arr.append(temp)

key = input('Enter key to search ')
linsearch(arr, key)
print(arr)
