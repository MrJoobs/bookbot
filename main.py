import sys
from stats import number_of_words, character_breakdown, sort_characters

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_text(sys.argv[1])
    word_count = number_of_words(book_text)
    char_counts = character_breakdown(book_text)
    sorted_chars = sort_characters(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    for item in sorted_chars:
        character = item["char"]
        count = item["count"]
        print(f"{character}: {count}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()