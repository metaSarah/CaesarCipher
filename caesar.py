
def encrypt(key,plaintext):
    
    ciphertext = ""
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in plaintext:
        index = (alphabet.find(letter) + key) % len(alphabet)
        
        ciphertext += alphabet[index]

    return ciphertext


def decrypt(key,ciphertext):
    
    plaintext = encrypt(26-key,ciphertext)

    return plaintext