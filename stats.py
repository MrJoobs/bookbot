def number_of_words(text):
    words = text.split()
    number = 0
    output = ""
    for word in words:
        number += 1
    output = f"{number} words found in the document"
    return output

def character_breakdown(text):
    text_lower = text.lower()
    char_counts = {}

    for char in text_lower:
        if char in char_counts:
            # Character already exists in dictionary, so increment its count
            char_counts[char] += 1
        else:
            # Character doesn't exist yet, so add it with count 1
            char_counts[char] = 1
    
    return char_counts