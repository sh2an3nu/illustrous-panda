def reverse(string):
    return string[::-1]
def isPalindrome(string):
    rev = reverse(string)
    if (rev==string):
        return True
    else:
        return False

