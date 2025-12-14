#Fahrenheit to Celsius Converter
#Goal: Write a function that takes a temperature in Fahrenheit as input and returns the temperature in Celsius.
#Formula: C = (F - 32) \times \frac{5}{9}

def Fahrenheit_to_Celsius_Converter(fehrenhiet:int)->float:
    celsius= (fehrenhiet-32)* 5/9
    return celsius


if __name__=="__main__":
    fehrenhiet= float(input("enter the temputer in Fahrenheit: "))
    result = Fahrenheit_to_Celsius_Converter(fehrenhiet)
    print(f"The result in celsius is: {round(result,2)}")