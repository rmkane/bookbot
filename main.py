#!/usr/bin/env python3


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_map = character_count(text)
    print(word_count)
    print(char_map)


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
