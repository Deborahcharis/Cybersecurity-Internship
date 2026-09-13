def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# Get input from user
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))

# Encryption
encrypted = encrypt(text, shift)

# Decryption
decrypted = decrypt(encrypted, shift)

# Display results
print("\nOriginal Text  :", text)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
