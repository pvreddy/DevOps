str1 = raw_input()

str2 = str1.split()
print str2
for i in range(1,len(str1)+1):
    if str2[i] == str2[i-1]:
        str2.remove(i)
        str2.remove(i+1)
    print str2
if str2 is not None:
    for i in str2:
        str1 = ''.join(i)
else:
    print('Empty String')
