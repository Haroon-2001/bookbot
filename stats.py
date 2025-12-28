# stats.py

def get_character_count(text):
    char_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


def sort_characters(char_count_dict):
    # Create list only from alphabetic characters
    char_list = []
    for char, count in char_count_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    # Helper function for sorting
    def get_num(item):
        return item["num"]
    
    # Sort descending (highest count first)
    char_list.sort(key=get_num, reverse=True)
    
    return char_list