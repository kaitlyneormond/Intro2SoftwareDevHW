#Author: Kaitlyn Ormond
#Date Written: 6/30/2024
#Assignment: Module 04 Programming Assignment 4-1
#This program takes a user inputted number and displays all of the prime numbers that
#are less than or equal to the number entered.

def is_prime(number):
    """
    Function to check if a number is prime.
    Returns True if the number is prime, otherwise False.
    """
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def display_primes(numbers):
    """
    Function to display the prime numbers from a list of numbers.
    """
    for num in numbers:
        if is_prime(num):
            print(num)

def main():
    """
    Main function to ask the user for an integer greater than 1,
    populate a list with integers from 2 to the entered number,
    and display all prime numbers from the list.
    """
    while True:
        try:
            user_input = int(input("Enter an integer greater than 1: "))
            if user_input > 1:
                break
            else:
                print("Please enter an integer greater than 1.")
        except ValueError:
            print("Invalid input. Please enter an integer greater than 1.")

    # Populate a list with integers from 2 to user_input
    numbers = list(range(2, user_input + 1))

    # Display prime numbers
    display_primes(numbers)

if __name__ == "__main__":
    main()
