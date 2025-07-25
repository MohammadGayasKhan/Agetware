'''Problem: Caesar Cipher encoding and decoding
In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code, or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. 
For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence
Write code that implements encoding and decoding of a message.
The parameters for the methods would be the message to be encoded / decoded and the length of the shift.'''

def caesar_cipher(message, shift):
    encoded_message = []
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encoded_message.append(new_char)
        else:
            encoded_message.append(char)
    return ''.join(encoded_message)

if __name__ == "__main__": 
    original_message = input("Enter the message to encode: ")
    shift_value = int(input("Enter the shift value: "))
    
    encoded = caesar_cipher(original_message, shift_value)
    print(f"Encoded Message: {encoded}")
    
    decoded = caesar_cipher(encoded, -shift_value)
    print(f"Decoded Message: {decoded}")  