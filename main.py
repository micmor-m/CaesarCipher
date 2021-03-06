import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)


def caesar(text_p, shift_p, direction_p):
    start_str = ""
    for ch in text_p:
        if ch in alphabet:
            if direction == "encode":
                new_index = shift_p + alphabet.index(ch)
                if new_index > 25:
                    new_index = new_index - 26
                start_str += alphabet[new_index]
            else:
                new_index = alphabet.index(ch) - shift_p
                start_str += alphabet[new_index]

    print(f"The {direction_p} text is {start_str}")


keep_going = "yes"
while keep_going == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26

    caesar(text, shift, direction)
    keep_going = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
