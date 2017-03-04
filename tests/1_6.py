from challenges.set1.challenge6 import hamming_distance, find_key_size, \
    find_key, decrypt


def hamming_distance_test():
    s1 = "this is a test"
    s2 = "wokka wokka!!!"
    expected = 37
    if hamming_distance(s1, s2) == expected:
        return True
    return False


def decrypt_test():
    f = open('../challenges/set1/challenge6/6.txt', 'r')
    cipher = f.read().decode("base64")
    key_size = find_key_size(2, 40, cipher)
    key = find_key(cipher, key_size)
    plaint_text = decrypt(cipher, key)

    return plaint_text


if __name__ == '__main__':
    print hamming_distance_test()
    print decrypt_test()
