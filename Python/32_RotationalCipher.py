def rotate(text, key):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters_cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters_list = list(letters)
    letters_list_cap = list(letters_cap)
    text_list = list(text)
    new_text = ""
    for char in text:
        if char.isupper():
            char_index_cap = letters_list_cap.index(char)
            new_index_cap = (letters_list_cap.index(char) + key) % 26
            new_char = letters_list_cap[new_index_cap]
            new_text += str(new_char)
            continue
        if char.islower():
            char_index = letters_list.index(char)
            new_index = (char_index + key) % 26
            new_char = letters_list[new_index]
            new_text += str(new_char)
            continue
        else:
            new_text += str(char)
            continue
    return new_text

