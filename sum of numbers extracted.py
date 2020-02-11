user_string = input()
numbers = [int(i) for i in user_string.split() if i.isdigit()]
print("Sum of numbers in string is:",(sum(numbers)))
