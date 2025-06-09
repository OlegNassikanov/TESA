# tesa.py - basic implementation of TESA (Tokenized Entity Semantic Abstraction)

def tokenize_text(text):
    markers = {"S1": "AI", "S2": "human", "S3": "interaction"}
    for marker, phrase in markers.items():
        text = text.replace(phrase, marker)
    return text

def detokenize_text(token_text, markers):
    for marker, phrase in markers.items():
        token_text = token_text.replace(marker, phrase)
    return token_text

# Example
text = "AI and human require interaction"
tokenized = tokenize_text(text)
print("Tokenized:", tokenized)    # Output: S1 and S2 require S3
print("Detokenized:", detokenize_text(tokenized, {"S1": "AI", "S2": "human", "S3": "interaction"}))