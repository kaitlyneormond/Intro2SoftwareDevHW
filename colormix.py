#Author: Kaitlyn Ormond
#Date Written: 6/16/24
#Assignment: Module 02 Programming Assignment 2-1
#This program takes two primary colors as input and outputs the secondary color.

color_set = set()

def color_check(colorA, colorB):

    """
    This function checks if the two colors are both primary colors,
    otherwise it returns False alongside an error message. If the same
    two colors are entered, it returns an error message.

    Parameters:
    colorA (str): The first color.
    colorB (str): The second color.

    Returns:
    bool: True if both colors are different primary colors, False otherwise.
    """
    
    valid_colors = ["red", "blue", "yellow"]
    
    if colorA not in valid_colors or colorB not in valid_colors:
        print("Error: Invalid color entered. Please enter a primary color.")
        return

    elif colorA == colorB:
        print("You have entered the same color twice. Please try again.")

    else:
        color_set.add(colorA)
        color_set.add(colorB)
        return color_set


def main():

    """
    This function prompts the user to enter two primary colors and displays 
    the resulting secondary color as long as both inputs are primary.
    """
    
    print("Welcome to the color mixing program.")
    print("Please enter two primary colors(red, blue, or yellow) to mix.")

    colorA = input("Please enter your first primary color: ")
    colorB = input("Please enter your second primary color: ")

    color_check(colorA, colorB)

    if "red" and "blue" in color_set:
        print("You have mixed purple.")
    elif "red" and "yellow" in color_set:
        print("You have mixed orange.")
    elif "blue" and "yellow" in color_set:
        print("You have mixed green.")

if __name__ == "__main__":
    main()