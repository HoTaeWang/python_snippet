import string

###################################################
# Function to encrypt a string using Caesar cipher
# Input: text, key
# Output: encrypted text
# Text: string to be encrypted
# key: number of positions to shift the letter
def cipher(text, key):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    encrypt =''
    for c in text:
        if c in uppercase:
            new = (uppercase.index(c) + key) % 26
            encrypt += uppercase[new]
        elif c in lowercase:
            new = (lowercase.index(c) + key) % 26
            encrypt += lowercase[new]
        else:
            encrypt += c

    return encrypt

# Test the function
print(cipher('Hello, World!', 3)) # Khoor, Zruog!
print(cipher('Khoor, Zruog!', -3)) # Hello, World!
print(cipher('Python is fun!', 5)) # Udymts nx kwu!
