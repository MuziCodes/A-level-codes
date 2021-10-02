# Input list and item-to-search (key)
a = [int(x) for x in input('Enter elements separated by space: ').split()]
key = int(input('Enter element to search: '))

# Then search one by one using for loop
for i in range(len(a)):
    if a[i] == key:
        print('key is at element', i + 1)  # +1 because loop starts at 0
        break
else:
    print(key, 'not available')
