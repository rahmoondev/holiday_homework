#​7. Reverse String Checker
# ​Goal: Write a function that checks if a string is a palindrome (reads the same forwards and backward, like "madam").
# Concepts: String indexing/slicing, conditional checks.
def is_palindrome(word):
    return word == word[::-1]

if __name__=="__main__":
    input=input("enter a word:")
    if is_palindrome(input):
        print(f"{input} is a palindrome.")
    else:
        print(f"{input} is not a palindrome")