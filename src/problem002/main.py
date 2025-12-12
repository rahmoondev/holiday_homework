#2. Simple Calculator
# Goal: Create a script that takes two numbers and an operator (like +, -, *, /) from the user and performs the calculation.
# Concepts: if/elif/else statements, input handling.

num1=float(input("enter a number: "))
num2=float(input("enter a 2nd number: "))
operator=input("enter an operator (+, -, *, /): ")

if operator=='+':
    print(num1+num2)
elif operator=='-':
    print(num1-num2)
elif operator=='*':
    print(num1*num2)
elif operator=='/':
    if num2!=0:
        print(num1/num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator.")