size = int(input("Enter size of stack: "))
stack = [None for i in range(size)]  # make empty stack with size of input
base = 0
top = -1  # so 1st element will be index 0 after top += 1 below

def push(value):
    global top  # global variable to affect outside function
    if top < size - 1:  # -1 since 1st index is 0, basically if top not max..
        top += 1
        stack[top] = value
    else:
        print("Overflow! cannot push.")

def pop():
    global top, base
    if top == base - 1:  # if stack empty
        print("Underflow! cannot pop.")
    else:
        print(stack[top], "is removed")  # optional
        stack[top] = None 
        top -= 1

# ///PSEUDOCODE\\\

# CONSTANT nullp = –1
# CONSTANT size = 8
# DECLARE base : INTEGER
# DECLARE top : INTEGER
# DECLARE Stack : ARRAY[1 : size – 1] OF STRING
# PROCEDURE InitialiseStack
#     base ← 0
#     top ← nullp
# ENDPROCEDURE

# PROCEDURE Push(value)
#     IF top < size – 1
#       THEN
#         top ← top + 1
#         Stack[top] ← value
#     ENDIF
# ENDPROCEDURE

# FUNCTION Pop()
#     DECLARE Item : STRING
#     Item ← ""
#     IF top > nullp
#       THEN
#         Item ← Stack[top]
#         top ← top – 1
#     ENDIF
#     RETURN Item
# ENDFUNCTION

# uses LIFO
