def linsearch(array, key):
    for i in range(len(array)):
        if array[i] == key:
            print('Found at position', i + 1)
            break
    else:
        print('Not found')

array = [] # empty list to append values
length = int(input('Enter length of list ')) # to determine index of loop

# append values using for-loop
for i in range(length):
    temp = input('Enter value ')
    array.append(temp)

key = input('Enter key to search ')
linsearch(array, key)
