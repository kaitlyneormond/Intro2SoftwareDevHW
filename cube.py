#Author: Kaitlyn Ormond
#Date Written: 6/9/24
#Assignment: Module 01 Practice Exercise 2-2
#This program takes the length of an edge (an integer) as input and prints the cube’s surface area as output.

def surface_area_calc(edge_length):
    """
    Calculate and return the surface area of a cube.

    Parameters:
    edge_length (integer): The length of an edge of the cube.

    Returns:
    Integer: The surface area of the cube.
    """
    return 6 * (edge_length ** 2)

def main():
    """
    A program that calculates the surface area of a cube.
    The user is prompted to input the length of the cube's edge.
    From there, the surface area is calculated using the following formula: surface area = 6 * edge_length^2.
    The result is displayed.
    """

    # Prompt the user to input the edge length of the cube
    edge_length = int(input("Please enter the length of the edge of the cube (in meters): "))

    # Calculating the surface area
    surface_area = surface_area_calc(edge_length)

    # Output the results
    print("The edge length (in meters) entered was: ", edge_length)
    print("The surface area (in square meters) is: ", surface_area)

if __name__ == "__main__":
    main()