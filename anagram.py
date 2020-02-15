"""anagram or not using sorted() method"""
def anagrams(s,s1):
    a = sorted(s)
    b = sorted(s1)
    if (a == b):
        print("Anagrams")
    else:
        print("Not Anagrams")