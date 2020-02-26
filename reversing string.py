import stack
s=input("Enter String to be reversed: ")
obj = Stack()
for i in s:
    obj.push(i)
while True:
    x=obj.pop()
    if x:
        print(x,end='')
    else:
        break