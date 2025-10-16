def remove_backspaces(text):
    
    for ch in text:
        if ch == "\b":
            index_of_slash = text.find(ch)
            text = text[:index_of_slash-1] + text[index_of_slash+1:]
         

    return text


# print(remove_backspaces("abc\b\bxyz"))

# "ersin\bersin\\b"