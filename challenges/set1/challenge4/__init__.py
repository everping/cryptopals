# Detect single-character XOR
from challenges.set1.challenge3 import break_single_byte_xor


def detect_single_character_xor(cipher_list):
    max_score = 0
    my_plain_text = ""
    for elm in cipher_list:
        plain_text, score = break_single_byte_xor(elm.strip())
        if score > max_score:
            max_score = score
            my_plain_text = plain_text
    return my_plain_text
