def linsearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print('Found at position', i + 1)
            break
    else:  # ← BEWARE of indentation
        print('Not found')

# Searches through all elements in list until value is found
# This means if item is at the last value, it will search the whole list.
# Binary search is a better alternative as it skips half the list.
# Order of growth/time complexity O(n) in Big O notation
