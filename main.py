#!/usr/bin/env python3


def main():
    generate_report("books/frankenstein.txt")


def generate_report(book_path):
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_map = character_count(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for ch, count in sorted(char_map.items(), key=lambda x: x[1], reverse=True):
        if ch.isalpha():
            print(f"The '{ch}' character was found {count} times")

    print(f"--- End of report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def character_count(text):
    char_map = {}
    for c in text.lower():
        char_map[c] = char_map.get(c, 0) + 1
    return char_map


def count_words(text):
    return len(text.split())


main()
