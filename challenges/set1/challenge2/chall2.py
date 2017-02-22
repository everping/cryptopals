# Fixed XOR
def xor(str1, str2):
    str1 = str1.decode('hex')
    str2 = str2.decode('hex')
    result = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2))
    return result.encode('hex')
