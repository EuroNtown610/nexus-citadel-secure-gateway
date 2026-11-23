def xor_cipher(data, key):
    if not key:
        return 'Key cannot be empty'
    result = []
    for i, char in enumerate(data):
        key_char = key[i % len(key)]
        xor_char = chr(ord(char) ^ ord(key_char))
        result.append(xor_char)
    return ''.join(result)
encrypted = xor_cipher('Anton-A380', 'Citadel')
print (repr(encrypted))