import stack
s=input("Enter the parantheses: ")
d={")":"(","]":"[","}":"{"}
obj = Stack()
for i in s:
    if i in ["(","{","["]:
        obj.push(i)
    else:
        x=obj.pop()
        if not x or x!=d[i]:
            print("Not Balanced")
            break
else:
    x=obj.pop()
    print("Balanced") if not x else print("Not Balanced")