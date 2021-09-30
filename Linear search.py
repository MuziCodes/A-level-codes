# Take an example list and key to search
a = [10, 20, 3, 44, 5, -6]
key = int(input('Enter element to search: '))

# Using For loop
for i in range(len(a)):  
    if a[i] == key:
        print('key is at element', i + 1) # +1 because loop starts at 0
        break
else:
    print(key, 'not available')

# Using While loop
i = 0
while i < len(a):
    if a[i] == key:
        print('key is at element', i + 1)
        break # stops further execution
    i += 1
else: # ← be careful of indentation
    print(key, 'not available')
