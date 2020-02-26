import stack
"""only for one kind of parantheses"""
s=input("Enter the parantheses: ")
obj = Stack()
for i in s:
    if i=="(":
        obj.push(i)
    else:
        x=obj.pop()
        if not x:
            print("Not Balanced")
            break
else:
    x=obj.pop()
    print("Balanced") if not x else print("Not Balanced")