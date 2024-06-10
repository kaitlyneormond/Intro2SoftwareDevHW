#Author: Kaitlyn Ormond
#Date Written: 6/9/24
#Assignment: Module 01 Programming Assignment 1-1
#This program calculates the total cost of a meal, including the cost of the meal, sales tax, and an 18% tip.

def calculate_tip(meal_cost, tip_rate):
    """
    Calculate the tip based on the meal cost and tip rate.
    
    Parameters:
    meal_cost (float): The cost of the meal.
    tip_rate (float): The tip percentage as a decimal.
    
    Returns:
    float: The tip amount.
    """
    return meal_cost * tip_rate

def calculate_tax(meal_cost, tax_rate):
    """
    Calculate the tax based on the meal cost and tax rate.
    
    Parameters:
    meal_cost (float): The cost of the meal.
    tax_rate (float): The tax percentage as a decimal.
    
    Returns:
    float: The tax amount.
    """
    return meal_cost * tax_rate

def main():
    """
    A program to calculate the total cost of a meal at a restaurant including tip and tax.
    """
    
    try:
        # Prompt user for the cost of the meal
        meal_cost = float(input("Enter the charge for the food: $"))
        
        # Constants for tip and tax rates
        TIP_RATE = 0.18
        TAX_RATE = 0.07
        
        # Calculate tip and tax
        tip = calculate_tip(meal_cost, TIP_RATE)
        tax = calculate_tax(meal_cost, TAX_RATE)
        
        # Calculate the total cost
        total_cost = meal_cost + tip + tax

        # Display the results
        print("Meal Cost: ", meal_cost)
        print("Tip (18%): ", tip)
        print("Tax (7%): ", tax)
        print("The total cost is: ", total_cost)

    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()