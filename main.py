from stats import number_of_words, character_breakdown

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = number_of_words(book_text)
    char_counts = character_breakdown(book_text)
    
    print(f"Word count: {word_count}")
    print(f"Character counts: {char_counts}")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()