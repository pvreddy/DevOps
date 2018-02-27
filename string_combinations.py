from itertools import permutations
s = raw_input("Please enter the string:")
#s = 'maadm'
comb_strs = strs = [''.join(p) for p in permutations(s)]
print comb_strs

for i in comb_strs:
    if i == i[::-1]:
        print i, ' is a palindrom'
        break
else:
    print i, " don't have a combination of palindrom"
