def reverse(text):
    reverse_string = ''
    for letter in text:
        reverse_string = letter + reverse_string
    return reverse_string
