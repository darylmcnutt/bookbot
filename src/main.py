from utils import *

print("### BookBot 9000 ###")
book_path = "../books/frankenstein.txt"

with open(book_path) as f:
    file_contents = f.read()
    print(count_words(file_contents))

