# Single-byte XOR cipher
from challenges.set1.challenge2.chall2 import xor

# http://www.data-compression.com/english.html
frequencies = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182
}


def score(str):
    score = 0
    for c in str:
        if c in frequencies:
            score += frequencies[c]
    return score


def break_xor(cipher):
    decoded_cipher = cipher.decode('hex')
    plain_text = ""
    max_score = 0

    for x in range(256):
        key = (chr(x) * len(decoded_cipher)).encode('hex')
        decoded_plain = xor(key, cipher).decode('hex')
        score_fred = score(decoded_plain)
        if score_fred > max_score:
            max_score = score_fred
            plain_text = decoded_plain

    return plain_text, max_score


