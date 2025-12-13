#​4. Factorial Calculator
# ​Goal: Write a program to calculate the factorial of a user-provided number (e.g., 5! = 5 \times 4 \times 3 \times 2 \times 1).
# Concepts: Loops (for or while), basic arithmetic.

number= int(input("Enter a number to calculate its factorial: "))
factorial=1
for i in range(1, number + 1):
    factorial *= i

print(f"The factotial for {number} is: {factorial}")


