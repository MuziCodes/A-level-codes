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

# ///PSEUDOCODE\\\

# Found ← FALSE
# low ← 0
# upp ← MaxIndex - 1  // MaxIndex is LENGTH(list)
# WHILE (low <= upp) AND NOT(Found) DO
#     mid ← (low + upp) DIV 2
#     IF list[mid] = key
#       THEN
#         Found ← TRUE
#         RETURN mid  // equivalent of break
#       ELSE
#         IF list[mid] < key
#           THEN
#             low ← mid + 1
#           ELSE
#             upp ← mid - 1
#         ENDIF
#     ENDIF
# ENDWHILE
# IF Found = FALSE
#     THEN
#       OUTPUT "Not found"
# ENDIF

# repeated checking of the middle item in an ordered search list and discarding the half
# of the list which does not contain the search item
# Order of growth/time complexity of O(Log₂ n) in Big O notation
# Has to be sorted before usage as the midpoint is the middle element not the average value
# it might even discard the value to search as the higher values will not be higher in reality.
