# Detect AES in ECB mode


def detect_aes_ecb(cipher):
    """
    1. Break cipher into blocks of 16 byte length
    2. If a block appears at least 2 times, it is the cipher that is looking for
    """
    assert len(cipher) % 16 == 0
    blocks = []
    while cipher:
        block = cipher[:16]
        if block in blocks:
            return True
        blocks.append(block)
        cipher = cipher[16:]
    return False
