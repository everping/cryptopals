from challenges.set1.challenge4 import detect_single_character_xor

f = open('../challenges/set1/challenge4/4.txt', 'r')
xored_list = f.readlines()
f.close()

print detect_single_character_xor(xored_list)
