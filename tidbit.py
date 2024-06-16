#Author: Kaitlyn Ormond
#Date Written: 6/16/24
#Assignment: Module 02 Practice Exercise 3-10
#This program takes the purchase price as input and displays a table 
#of a payment schedule for the lifetime of the loan.
#It includes the month number (beginning with 1), the current total balance owed
#the interest owed for that month, the amount of principal owed for that month
#the payment for that month, and the balance remaining after payment.


ANNUAL_RATE = 0.12
MONTHLY_RATE = ANNUAL_RATE / 12
DOWNPAYMENT_RATE = 0.10
TABLEFORMATSTRING = "%2d%15.2f%15.2f%17.2f%17.2f%17.2f"

def main():

    """
    A program that calculates the monthly payment and interest and displays
    the payment plan for a loan, taking the purchase price as input.

    Parameters:
    None
    
    Returns:
    None
    """

    fltPurchasePrice = float(input("Enter the purchase price: "))

    monthlyPayment = 0.05 * fltPurchasePrice
    month = 1
    balance = fltPurchasePrice - (fltPurchasePrice * DOWNPAYMENT_RATE)

    print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")
    while balance > 0:
        if monthlyPayment > balance:
            monthlyPayment = balance
            interest = 0
        else:
            interest = balance * MONTHLY_RATE
        principal = monthlyPayment - interest
        remaining = balance - monthlyPayment
        print(TABLEFORMATSTRING % (month, balance, interest, principal, monthlyPayment, remaining))
        balance = remaining
        month += 1

if __name__ == "__main__":
    main()
