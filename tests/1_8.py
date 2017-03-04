from challenges.set1.challenge8 import detect_aes_ecb

if __name__ == '__main__':
    f = open('../challenges/set1/challenge8/8.txt', 'r')
    content = f.readlines()
    f.close()
    for line in content:
        cipher = line.strip().decode('hex')
        if detect_aes_ecb(cipher):
            print line
