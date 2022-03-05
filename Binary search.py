def binsearch(arr, key):
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
    else:  # ← BEWARE of indentation
        print('Not found')

# repeated checking of the middle item in an ordered search list and discarding the half
# of the list which does not contain the search item
# Order of growth/time complexity of O(Log₂ n) in Big O notation
# Has to be sorted before usage as the midpoint is the middle element not the average value
# it might even discard the value to search as the higher values will not be higher in reality.
