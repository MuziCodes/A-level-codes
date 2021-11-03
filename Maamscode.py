def push(item):
    global top,n
    print("stack size is:",n,"and top is:",top)
    if top<n-1:
        top=top+1
        st[top]=item
    else:
        print("Overflow")
    print(st)
        
   
def pop():
    global top,base,item
    if top==base-1:
        print("Underflow")
    else:
        item=st[top]
        st[top]="*"
        top=top-1
        print(item, "is removed")
        
   
def display():
    global top
    print(st)
    print("[",end=" ")
    
    for i in range(0,top+1):
        print(st[i],end=" ")
    print("]")
    
n=int(input("Enter the size of the stack:"))    
st=["*" for index in range(0,n)]
item=None
top=-1
 
base=0
top=-1
c='y'
sf=10
print()
while c=='y':
    print("Stack Operations")
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    ch=int(input("Enter your choice:"))
    if ch==1:
        item=int(input("Enter the item to be pushed:"))
        push(item)
    elif ch==2:
        pop()
    elif ch==3:
        display()
    else:
        print("Please enter a proper choice")
    c=input("Do you want to continue?")
 
Muzammil Ahmed
