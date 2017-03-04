from challenges.set1.challenge5 import repeating_key_xor
from challenges.set1.challenge3 import score


def hamming_distance(s1, s2):
    """Count the # of differences between equal length strings str1 and str2"""
    assert len(s1) == len(s2)
    bin_string = map(lambda s: (''.join('{0:08b}'.format(x, 'b') for x in bytearray(s))), [s1, s2])
    return sum(ch1 != ch2 for ch1, ch2 in zip(bin_string[0], bin_string[1]))


def normalized_hamming_distance(key_size, cipher):
    """
    Calculate the normalized hamming distance
    """
    nhd = 0
    pair_no = len(cipher) / (key_size * 2)
    for no in xrange(pair_no):
        nhd += hamming_distance(cipher[:key_size], cipher[key_size:key_size * 2])
        cipher = cipher[key_size * 2:]
    return nhd / (pair_no * float(key_size))


def find_key_size(min_key_size, max_key_size, cipher):
    return min(xrange(min_key_size, max_key_size),
               key=lambda x: normalized_hamming_distance(x, cipher))


def find_key(cipher, key_size):
    """
    1. Break the cipher into blocks of key_size length
    2. Transpose blocks
    3. For each block, we xor it with printable characters
    and then score the output, get the character that has max score.
    4. Form the key by joining the characters that we have found
    """
    key = ""

    for i in range(key_size):
        transposed_block = cipher[i::key_size]
        key += chr(max(range(256),
                       key=lambda k: score(repeating_key_xor(transposed_block, chr(k)).decode('hex'))))
    return key


def decrypt(cipher, key):
    return repeating_key_xor(cipher, key).decode('hex')
