def linsearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print('Found at position', i + 1)
            break
    else:  # ← BEWARE of indentation
        print('Not found')
