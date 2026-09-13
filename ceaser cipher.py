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



text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))


encrypted = encrypt(text, shift)


decrypted = decrypt(encrypted, shift)


print("\nOriginal Text  :", text)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
