#Author: Kaitlyn Ormond
#Date Written: 6/9/24
#Assignment: Module 01 Programming Assignment 1-1
#This program converts celsius to fahrenheit.

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from celsius to fahrenheit.

    Parameters:
    celsius (float): The temperature in degrees celsius.

    Returns:
    float: The temperature in degrees fahrenheit.
    """
    return (9/5) * celsius + 32

def main():
    """
    A program that converts temperatures from celsius to fahrenheit.
    """

    try:
        celsius = float(input("Enter temperature in Celsius: "))

        fahrenheit = celsius_to_fahrenheit(celsius)

        print("The temperature in Fahrenheit is: ", fahrenheit)

    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()