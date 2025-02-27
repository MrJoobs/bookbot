def main():
    text, number_of_words = get_book_text("books/frankenstein.txt")
    print(number_of_words)

def get_book_text(filepath):
    output = ""
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    output = number_of_words(file_contents)
    return file_contents, output

def number_of_words(text):
    words = text.split()
    number = 0
    output = ""
    for word in words:
        number += 1
    output = f"{number} words found in the document"
    return output

main()