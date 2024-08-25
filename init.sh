#!/usr/bin/env bash

# A script to download Frankenstein from <https://github.com/asweigart/codebreaker>

book_repo=https://raw.githubusercontent.com/asweigart/codebreaker
books=("frankenstein.txt")

setup() {
    if [ ! -d "books" ]; then
        mkdir books
    fi
}

download_book() {
    local book=$1

    if [ -f "books/$book" ]; then
        echo "Skipping download of $book because it already exists."
        return
    fi

    echo "Downloading $book..."
    if curl -s -o "books/$book" "$book_repo/master/$book"; then
        echo "$book downloaded successfully."
    else
        echo "Failed to download $book."
    fi
}

# Main
setup
for book in "${books[@]}"; do
    download_book "$book"
done
