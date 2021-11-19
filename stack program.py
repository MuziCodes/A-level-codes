size = int(input("Enter size of stack: "))
stack = [None for index in range(size)]  # make empty stack with size of input
base = 0
top = -1  # so 1st element will be index 0 after top += 1 below
item = None  # initialise item to push

def push(item):
    global top  # global variable to affect outside function
    if top < size - 1:  # -1 since 1st index is 0, basically if top not max..
        top += 1  # top = top + 1
        stack[top] = item
    else:
        print("Overflow! cannot push.", stack)

# ALTERNATIVE:
# if len(stack) == size:
#     print("Overflow! cannot push.", stack)
# else:
#     stack.append(item)

def pop():
    global top, base, item
    if top == base - 1:  # basically if stack empty
        print("Underflow! cannot pop.")
    else:
        item = stack[top]
        stack[top] = None  # replace empty element with None for display
        top = top - 1
        print(item, "is removed")

# ALTERNATIVE:
# if len(stack) == 0:
#   print("Underflow! cannot pop.")
# else:
#   stack = stack[:-1]

while True:  # runs infinitely until break
    option = int(input("""Choose an option:
(1) Push
(2) Pop
(3) Display stack
(4) Exit
→ """))

    if option == 1:
        item = input("Enter item to push: ")
        push(item)
    elif option == 2:
        pop()
    elif option == 3:
        print(stack)
    elif option == 4:
        break
    else:
        print("Please enter a number between 1-4")
