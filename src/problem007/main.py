#​7. Reverse String Checker
# ​Goal: Write a function that checks if a string is a palindrome (reads the same forwards and backward, like "madam").
# Concepts: String indexing/slicing, conditional checks.
def is_palindrome(s):
    return s == s[::-1]

input=input("enter a string:")
if is_palindrome(input):
    print(f"{input} is a palindrome.")
else:
    print(f"{input} is not a palindrome")