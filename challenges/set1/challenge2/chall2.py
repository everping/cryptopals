# Fixed XOR
def xor(s1, s2):
    """
    Do XOR two hex-string and return a hex-string
    """
    s1 = s1.decode('hex')
    s2 = s2.decode('hex')
    result = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))
    return result.encode('hex')
