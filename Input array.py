arr = []
size = int(input('Enter length of list: '))
# append values to empty list using for-loop
for i in range(size):
    temp = int(input('Enter element to add: '))
    arr.append(temp)  # arr[size:size] = temp appends using slicing

# ALTERNATIVE:
# 
# print('Enter values separated by spaces')
# arr = [int(i) for i in input().split()]
# remove int() for string values
