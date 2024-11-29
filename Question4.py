# 2. Write a Python function that checks whether a word or phrase is palindrome or
# not.
# Note: A palindrome is word, phrase, or sequence that reads the same
# backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"
# 3. Write a Python function to check whether a string is pangram or not. (Assume
# the string passed in does not have any punctuation)
# Note: Pangrams are words or sentences containing every letter of the
# alphabet at least once. For example: "The quick brown fox jumps over the
# lazy dog"
# 4. Write a program that takes an integer as input and returns an integer with
# reversed digit ordering.
# Examples:
# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19.



def reverse_integer(n):
    if n < 0:
 
        reversed_num = int(str(-n)[::-1])
        return -reversed_num
    else:
        reversed_num = int(str(n)[::-1])
        return reversed_num

# Test cases
print(reverse_integer(500)) 
print(reverse_integer(-56))  
print(reverse_integer(-90))  
print(reverse_integer(91))   
