def custom_tokenization(input_text):
    tokens = []
    current_token = ""

    for char in input_text:
        if char.isalnum() or char == " ":
            current_token += char
        elif current_token:
            tokens.append(current_token)
            current_token = ""
    
    if current_token:
        tokens.append(current_token)
    
    return tokens

def tokenise_all_char(input_text):
    return list(input_text)

if __name__ == "__main__":
    input_text = input("Enter text for tokenization: ")
    
    word_tokens = custom_tokenization(input_text)
    char_tokens = tokenise_all_char(input_text)
    
    print("Tokenized word text:")
    print(word_tokens)
    print("Tokenized char text:")
    print(char_tokens)
