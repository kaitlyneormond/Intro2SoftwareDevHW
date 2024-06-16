#Author: Kaitlyn Ormond
#Date Written: 6/16/24
#Assignment: Module 02 Programming Assignment 2-2
#This program takes one non-negative number and finds the factorial of that number.

def factorial(n):

    """
    This function takes one non-negative number and finds the factorial of that number.

    Parameters:
    n (int): The number to find the factorial of.

    Returns:
    None.
    """
    
    product = 1
    for i in range(1, n+1):
        product = product * i
    print(product)

def main():

    """
    This function takes one non-negative number and finds the factorial of that number.

    Parameters:
    None.

    Returns:
    None.
    """
    
    n = int(input("Enter a non-negative number: "))
    factorial(n)

if __name__ == "__main__":
    main()