# main.py
from stats import get_character_count, sort_characters
import sys

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def main():
    # 1. Check if we have exactly one argument (besides the script name)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with error code 1

    # 2. Get the book path from command line argument
    book_path = sys.argv[1]
    
    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: File not found: {book_path}")
        sys.exit(1)
    
    num_words = count_words(text)
    char_counts = get_character_count(text)
    sorted_chars = sort_characters(char_counts)
    
    # Print exact report format
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()