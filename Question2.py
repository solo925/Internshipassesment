# 2. Write a Python function that checks whether a word or phrase is palindrome or
# not.
# Note: A palindrome is word, phrase, or sequence that reads the same
# backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"


def is_palindrome(s):
    clean_s = s.replace(" ", "").lower()
    return clean_s == clean_s[::-1]

# example test
print(is_palindrome("madam")) 
print(is_palindrome("nurses run"))  
print(is_palindrome("hello")) 
