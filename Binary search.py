def binsearch(arr, key):
    """Binary search works on sorted list"""
    lowB = 0       # lower bound
    upB = len(arr) - 1 # upper bound
    
    while lowB <= upB:
        mid = (lowB + upB) // 2 # int of mid value
        if arr[mid] == key:
            print('key is at element', mid + 1)
            break
        elif arr[mid] < key: # if key at right of list
            lowB = mid + 1
        else:              # if key at left of list
            upB = mid - 1
    else:
        print('Not found')
