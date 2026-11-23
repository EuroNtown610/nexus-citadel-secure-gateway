def caesar(user_message, key, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyz' 
    if type(key) != int or key < 1:
        return 'shift must be a positive integer'
    key = key % 26
    if not encrypt: 
        key = -key
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return user_message.translate(translation_table)
message = input('Enter your message: ')
shift = int(input('Enter your shift key(number): '))
mode = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
is_encrypt = (mode == 'e')
result = caesar(message, shift, encrypt=is_encrypt)
print(result)