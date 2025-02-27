def number_of_words(text):
    words = text.split()
    number = 0
    output = ""
    for word in words:
        number += 1
    output = f"Found {number} total words"
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

def sort_on(dict):
    return dict["count"]

def sort_characters(dictionary):
    output_list = []
    for character in dictionary:
        if character.isalpha():
            processed_dictionary = {
                "char" : character,
                "count" : dictionary[character]
            }
            output_list.append(processed_dictionary)
    output_list.sort(reverse=True,key=sort_on)
    return output_list
