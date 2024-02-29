from crypto.Cipher import AES
from crypto import Random
import binascii


def append_space_padding(str, blocksize=128):
    pad_len = blocksize - (len(str) % blocksize)
    padding = 'a'*pad_len
    return str + padding

def remove_space_padding(str, blocksize=128):
    pad_len = 0

    for char in str[::-1]:
        if char == 'a':
            pad_len += 1
        else:
            break
    
    return str[:-pad_len]

def encrypt(plaintext, key):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.encrypt(plaintext)

def decrypt(ciphertext, key):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.decrypt(ciphertext).decode('UTF-8')

if __name__ == "__main__":
    # key is 128 bits - 16 bytes
    key = Random.new().read(16)

    print("key: %s" % key.encode('hex'))

    plaintext = "This is the secret message we want to encrypt"

    print("length of plaintext: %d" % len(plaintext))
    print("plaintext: %s" % plaintext)

    paddedtext = append_space_padding(plaintext)

    print("length of paddedtext: %d" % len(paddedtext))
    print("paddedtext: %s" % paddedtext)

    ciphertext = encrypt(paddedtext, key)

    print("hexified ciphertext: %s" % binascii.hexlify(bytearray(ciphertext)))

    decrypted = decrypt(ciphertext, key)
    maybe_plaintext = remove_space_padding(decrypted)
    
    print("decrypted text: %s" % maybe_plaintext)