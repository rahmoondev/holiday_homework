#Fahrenheit to Celsius Converter
#Goal: Write a function that takes a temperature in Fahrenheit as input and returns the temperature in Celsius.
#Formula: C = (F - 32) \times \frac{5}{9}

def Fahrenheit_to_Celsius_Converter():
    f= float(input("enter the temputer in Fahrenheit: "))
    c= (f-32)* 5/9
    print(c) 

Fahrenheit_to_Celsius_Converter()