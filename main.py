def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents


def main():
    book = get_book_text('./books/frankenstein.txt')

    print(book)

main()
