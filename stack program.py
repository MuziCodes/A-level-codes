size = int(input('Size of stack? : '))
arr = [None for i in range(size)]
while True:
    option = int(input('''Choose an option:
(1) Push
(2) Pop
(3) Display stack
(4) Exit
→ '''))

    if option == 1:  # Push
        if None not in arr:
            print('\nOverflow! can\'t push.\n')
        else:
            value = input('Enter value to push: ')
            arr[arr.index(None)] = value
    elif option == 2:  # Pop
        if None not in arr:
            arr[-1] = None
        elif arr.index(None) != 0:
            arr[arr.index(None) - 1] = None
        else:
            print("\nUnderflow! can't pop.\n")
    elif option == 3:  # Display stack
        print(f'\n {arr}\n')
    elif option == 4:  # Exit
        break
