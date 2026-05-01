def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents

def get_number_of_words(path_to_book):
    book = get_book_text(path_to_book)
    words = book.split()
    return len(words)

