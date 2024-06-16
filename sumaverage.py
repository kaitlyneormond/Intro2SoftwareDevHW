def average(theSum, count):

    """ 
Calculate the average of numbers inputted by theuser, variable theSum, 
dividing by the count of numbers inputted by the user, variable count.

Parameters:
theSum: the sum of all the numbers inputted by the user
count: the count of all the numbers inputted by the user

Returns:
The average of the numbers inputted by the user """
    
    if count != 0:
        return theSum / count
    else:
        return 0
def main():

    """
The main function of the program. It will continue to loop, taking input from the user, 
until the user input an empty string. With each input, the number is added to the sum as variable theSum.
The count is incremented by 1. The average is calculated and printed.
"""
    theSum = 0
    count = 0

    
    while True:
        num = input("Enter a number or press Enter to quit: ")
        if num == "":
            break
        theSum += float(num)
        count += 1

    print("The sum is: ", theSum)
    print("The average is: ", average(theSum, count))

if __name__ == "__main__":
    main()