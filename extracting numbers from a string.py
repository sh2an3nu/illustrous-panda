user_string = input()
numbers = [int(i) for i in user_string.split() if i.isdigit()]
print("Numbers in the given string are:",str(numbers))