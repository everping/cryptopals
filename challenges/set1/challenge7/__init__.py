# AES in ECB mode
from Crypto.Cipher import AES


def aes_128_ecb_decrypt(cipher, key):
    encryptor = AES.new(key, AES.MODE_ECB)
    plaintext = encryptor.decrypt(cipher)
    return plaintext
