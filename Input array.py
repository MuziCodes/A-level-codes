arr = []
length = int(input('Enter length of list: '))

# append values to empty list using for-loop

for i in range(length):
    temp = int(input('Enter element to add: '))
    arr.append(temp)

# ALTERNATIVE:
# arr = [int(i) for i in input('Enter elements seperated by spaces: ').split()]
# remove int() for string values
