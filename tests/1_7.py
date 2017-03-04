from challenges.set1.challenge7 import aes_128_ecb_decrypt

if __name__ == '__main__':
    f = open('../challenges/set1/challenge7/7.txt', 'r')
    cipher = f.read().decode("base64")
    key = "YELLOW SUBMARINE"
    print aes_128_ecb_decrypt(cipher, key)
