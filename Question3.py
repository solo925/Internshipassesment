# 2. Write a Python function that checks whether a word or phrase is palindrome or
# not.
# Note: A palindrome is word, phrase, or sequence that reads the same
# backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"
# 3. Write a Python function to check whether a string is pangram or not. (Assume
# the string passed in does not have any punctuation)
# Note: Pangrams are words or sentences containing every letter of the
# alphabet at least once. For example: "The quick brown fox jumps over the
# lazy dog"


import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase) 
    return alphabet.issubset(set(s.lower()))  

# Test cases
print(is_pangram("The quick brown fox jumps over the lazy dog")) 
print(is_pangram("Hello World")) 
print(is_pangram("A quick brown fox jumps over the lazy dog")) 
print(is_pangram("The quick brown fox jumps over the lazy cat")) 