# Implement repeating-key XOR
from challenges.set1.challenge2.chall2 import xor


def repeating_key_xor(s, key):
    multiples = len(s) / len(key) + 1
    real_key = (key * multiples)[:len(s)]
    return xor(real_key.encode('hex'), s.encode('hex'))
