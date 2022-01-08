size = int(input("Enter size of stack: "))
stack = [None for i in range(size)]  # make empty stack with size of input
base = 0
top = -1  # so 1st element will be index 0 after top += 1 below

def push(item):
    global top  # global variable to affect outside function
    if top < size - 1:  # -1 since 1st index is 0, basically if top not max..
        top += 1
        stack[top] = item
    else:
        print("Overflow! cannot push.")

def pop():
    global top, base
    if top == base - 1:  # if stack empty
        print("Underflow! cannot pop.")
    else:
        print(stack[top], "is removed")  # optional
        stack[top] = None 
        top = top - 1

while True:  # runs infinitely until break
    option = int(input(f"""Choose an option:
(1) Push
(2) Pop
(3) Exit
{stack[base:top + 1]}  # doesn't show None, optional. {stack} is minimum
→ """))

    if option == 1:
        item = input("Enter item to push: ")
        push(item)
    elif option == 2:
        pop()
    elif option == 3:
        break
    else:
        print("Please enter a number between 1-4")
