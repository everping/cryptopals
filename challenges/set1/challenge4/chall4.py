# Detect single-character XOR
from challenges.set1.challenge3.chall3 import break_xor


def break_xors(xored_list):
    max_score = 0
    my_plain_text = ""
    for elm in xored_list:
        plain_text, score = break_xor(elm.strip())
        if score > max_score:
            max_score = score
            my_plain_text = plain_text
    return my_plain_text
