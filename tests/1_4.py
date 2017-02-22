from challenges.set1.challenge4.chall4 import break_xors

f = open('../challenges/set1/challenge4/4.txt', 'r')
xored_list = f.readlines()
f.close()

print break_xors(xored_list)
