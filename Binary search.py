a = [int(x) for x in input('Enter elements seperated by space\n').split()]
key = int(input('Enter element to search: '))

low = 0
high = len(a)-1

while low <= high:
    mid = (low + high) // 2
    if a[mid] == key:
        print('key is at element', mid + 1)
        break
    elif a[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print('Not found')
