from src.utils import *

print("### BookBot 9000 ###")
book_path = "books/frankenstein.txt"
print(f"--- Begin report of {book_path} ---")
with open(book_path) as f:
    file_contents = f.read()
    word_count = count_words(file_contents)
    letter_count = count_letters(file_contents)
letter_items = [{'char': c, 'count': n} for c, n in letter_count.items()]
sorted_letters = sorted(letter_items, key=sort_on, reverse=True)

display_results(word_count, sorted_letters)