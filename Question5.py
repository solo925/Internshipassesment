# 5. Write a program that accepts a string as input, capitalizes the first letter of each
# word in the string, and then returns the result string.
# Examples:
# "hi"=> returns "Hi"
# "i love programming"=> returns "I Love Programming"

def capitalize_words(s):
    return s.title()

# Test cases
print(capitalize_words("hi")) 
print(capitalize_words("i love programming"))  
