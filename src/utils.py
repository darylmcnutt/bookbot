def count_words(file):
    words = file.split()
    return len(words)

def count_letters(file):
    letter_dict = {}
    for letter in file:
        lowercase_letter = letter.lower()
        if lowercase_letter in letter_dict:
            letter_dict[lowercase_letter] += 1
        else:
            letter_dict[lowercase_letter] = 1
    return letter_dict

def display_results(word_count, sorted_letters):
    print(f"{word_count} words found in document")
    for i in sorted_letters:
        if i['char'].isalpha():
            print(f"The '{i['char']}' character was found {i['count']} times")

def sort_on(dict):
    return dict["count"]