from collections import Counter
import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    if not text:
        print("No report generated. The document could not be read.")
        return
    lowered_text = text.lower()
    print(f"--- Begin report of {book_path} ---")
    print(f"\nWord count in document: {count_words(text)}\n")
    letter_count = count_letters(lowered_text)
    sorted_count_list = letter_count_to_sorted_list(letter_count)
    for letter in sorted_count_list:
        print(f"The '{letter['letter']}' character was found {letter['num']} times")


def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return ""

def count_words(book):
    return len(book.split())

def count_letters(book):
    # Create a dictionary to store letter counts
    letter_counts = Counter(letter for letter in book if letter in string.ascii_lowercase)
    return letter_counts #if required at a later date

def letter_count_to_sorted_list(letter_counts):
    dictionary_list = []
    for key, value in letter_counts.items():
        entry_to_dict = {"letter": key, "num": value}
        dictionary_list.append(entry_to_dict)
    dictionary_list = sorted(dictionary_list, key=lambda x: x["num"], reverse=True)
    return(dictionary_list)



main()
