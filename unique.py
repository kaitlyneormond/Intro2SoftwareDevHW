#Author: Kaitlyn Ormond
#Date Written: 6/30/2024
#Assignment: Module 04 Practice Exercise 5-7
#Program that reads a file, extracting each unique word, sorts them alphabetically, and outputs the result.

def main():
    """
    Main function to read a file, extract unique words,
    sort them, and print each unique word.
    """
    
    in_name = input("Enter the input file name: ")
    
    unique_words = []

    try:
        with open(in_name, 'r') as input_file:

            for line in input_file:
                words = line.split()
                
                for word in words:
                    if word not in unique_words:
                        unique_words.append(word)
                        
    except FileNotFoundError:
        print(f"File {in_name} not found.")
        return

    unique_words.sort()

    for word in unique_words:
        print(word)

if __name__ == "__main__":
    main()