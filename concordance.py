#Author: Kaitlyn Ormond
#Date Written: 6/30/2024
#Assignment: Module 04 Practice Exercise 5-8
#This program reads a text file, counts the frequency of each unique word,
#sorts alphabetically, and outputs each unique word alongside its frequency.
def main():
    """
    Main function to read a file, count the frequency of each unique word,
    sort the words alphabetically, and print each word with its frequency.
    """

    in_name = input("Enter the input file name: ")
    unique_words = {}
    try:
        with open(in_name, 'r') as input_file:
            for line in input_file:
                words = line.split()

                for word in words:
                    if word in unique_words:
                        unique_words[word] += 1
                    else:
                        unique_words[word] = 1
    except FileNotFoundError:
        print(f"File {in_name} not found.")
        return

    word_list = list(unique_words.keys())
    word_list.sort()

    for word in word_list:
        print(f"{word}: {unique_words[word]}")

if __name__ == "__main__":
    main()