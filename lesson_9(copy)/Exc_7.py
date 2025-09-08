def caesar_cipher_simple(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def encrypt_file_simple(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    encrypted = []
    for i, line in enumerate(lines, 1):
        encrypted.append(caesar_cipher_simple(line.strip(), i))

    return encrypted

encrypted_text = encrypt_file_simple('Caesar.txt')
for line in encrypted_text:
    print(line)