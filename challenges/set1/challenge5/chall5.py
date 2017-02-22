# Implement repeating-key XOR
from challenges.set1.challenge2.chall2 import xor


def key_xor(str, key):
    multiples = len(str) / len(key) + 1
    real_key = (key * multiples)[:len(str)]
    print str
    print real_key

    return xor(real_key.encode('hex'), str.encode('hex'))
