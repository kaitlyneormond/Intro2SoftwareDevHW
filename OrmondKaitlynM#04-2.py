#Author: Kaitlyn Ormond
#Date Written: 6/30/2024
#Assignment: Module 04 Programming Assignment 4-2
#Sorts the prices of a shop's inventory, dipslays the top three prices
def sort_items_by_price(shop_items):
    """
    Function to sort items by price in descending order.
    Returns a list of tuples containing item names and their prices.
    """
    items_list = list(shop_items.items())

    # Sort items by price in descending order
    for i in range(len(items_list) - 1):
        for j in range(i + 1, len(items_list)):
            if items_list[i][1] < items_list[j][1]:
                items_list[i], items_list[j] = items_list[j], items_list[i]
    return items_list


def main():
    """
    Main function to get the top three items by price from a shop's inventory.
    """
    # Sample data
    shop_items = {
        'Apple': 0.50,
        'Banana': 0.20,
        'Mango': 0.99,
        'Coconut': 2.99,
        'Pineapple': 3.99
    }

    # Sort the items by price and get the top three
    sorted_items = sort_items_by_price(shop_items)
    top_items = sorted_items[:3]

    for item, price in top_items:
        print(f"{item}: {price:.2f}")

if __name__ == "__main__":
    main()