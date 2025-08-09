from stats import get_num_words
from stats import count_chars
from stats import sort_chars
import sys

def get_book_text(filepath):
    contents = None
    with open(filepath, encoding="utf8") as f:
        contents = f.read()
    return contents

def pretty_print_dict(dict):
    for key in dict:
        print(f"{key}: {dict[key]}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    # Print Report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    pretty_print_dict(sort_chars(count_chars(book_text)))

if __name__ == "__main__":
    main()