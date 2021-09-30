# Take a sample list
a = [10, 20, 3, 44, 5, -6]

# Use For-loop
for i in range(len(a)-1, 0, -1): # -1 as it starts from 0
    for j in range(i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j] # Swap

# Reverse Bubble sort
for i in range(len(a)):
    for j in range(i):
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
