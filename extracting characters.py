user_string = input("Enter a string: ")
result = ""
for i in user_string:
    if i.isalpha():
        result=" ".join([result,i])
print(str(result))