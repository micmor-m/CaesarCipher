alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text_p, shift_p):
    encrypt_str = ""
    for ch in text_p:
        new_index = shift_p + alphabet.index(ch)
        if new_index > 25:
            new_index = new_index - 26
        encrypt_str += alphabet[new_index]
    print(f"The encoded text is {encrypt_str}")


encrypt(text, shift)
