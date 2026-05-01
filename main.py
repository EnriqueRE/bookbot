from stats import get_number_of_words

def main():

    num_words = get_number_of_words('./books/frankenstein.txt')
    words = f"Found {num_words} total words"
    print(words)


main()
