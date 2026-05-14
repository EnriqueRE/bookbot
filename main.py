from stats import get_number_of_words, get_chars_dict

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents

def main():

    book_content = get_book_text('./books/frankenstein.txt')
    num_words = get_number_of_words(book_content)
    words = f"Found {num_words} total words"
    print(words)

    chars_dict = get_chars_dict(book_content)
    print(chars_dict)


main()
