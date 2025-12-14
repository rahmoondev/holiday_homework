#​4. Factorial Calculator
# ​Goal: Write a program to calculate the factorial of a user-provided number (e.g., 5! = 5 \times 4 \times 3 \times 2 \times 1).
# Concepts: Loops (for or while), basic arithmetic.
def  Factorial_Calculator(num:int):
    factorial=1
    for i in range(1, num + 1):
        factorial *= i
    return factorial


if __name__=="__main__":
    number= int(input("Enter a number to calculate its factorial: "))
    Factorial_number=Factorial_Calculator(number)
    print(f"The factotial for {number} is: {Factorial_number}")
