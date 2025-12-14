#2. Simple Calculator
# Goal: Create a script that takes two numbers and an operator (like +, -, *, /) from the user and performs the calculation.
# Concepts: if/elif/else statements, input handling.
def calculator():
    while True:
        num1=input("enter a number(type exit to exit): ")
        if num1=="exit":
            break
        num1= float(num1)
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


if __name__ == "__main__":
    calculator()