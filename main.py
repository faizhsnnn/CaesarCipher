from askii import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True

def caesar(orignal_text,shift_ammount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
            shift_ammount *= -1
    for letter in orignal_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter)+shift_ammount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        

    print(f"Here is the {encode_or_decode}d result: {cipher_text}")
        
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
    text = input("Type your message\n").lower()
    shift = int(input("Type shift number\n"))
    caesar(text,shift,direction)
    restart = input("Type 'yes' if you want to go again . otherwise type 'no'\n").lower()
    if restart == "no":
        should_continue = False
        print("Good Bye!")