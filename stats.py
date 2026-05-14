def get_number_of_words(book_content):
    words = book_content.split()
    return len(words)

def get_chars_dict(book_content):
    chars = list(book_content.lower())
    chars_dict = {}

    for char in chars:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1

    chars_dict.sort()

    return chars_dict


"""


    Add a new function to your stats.py file that takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
        Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
        Use the .sort() method:
            Use a helper function to return the "num" key of each dictionary for comparison.
            Sort the list from greatest to least by the count.
    Import and call the function in main.py, and capture the result.
    Print the report to the console as shown above. If the character is not an alphabetical character (using the .isalpha() method), just skip it. (Be sure to match the expected output in the CLI tests!)

    """"

