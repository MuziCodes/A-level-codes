def bubsort(arr):
    for i in range(len(arr)-1):  # 2nd last element so -1
        for j in range(len(arr)-i-1):  # ignore sorted so -i-1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
    # arr[:] = arr[::-1] here for descending order

# ///PSEUDOCODE\\\

# n ← MaxIndex - 1
# FOR i ← 0 TO MaxIndex - 1
#   FOR j ← 0 TO n
#     IF List[j] > List[j + 1]
#       THEN
#         Temp ← List[j]
#         List[j] ← List[j + 1]
#         List[j + 1] ← Temp
#     ENDIF
#   ENDFOR
#   n ← n - 1
# ENDFOR

# this code is inefficient as iterations continue even after array is sorted
# to enhance, use a flag to indicate if any swaps have taken place.
# if inner loop has made all comparisions with no changes, set flag to true
# Has order of growth/time complexity as O(n²) but O(n) if list already sorted
# Goes through all elements and swaps by comparing with next value for each pass
