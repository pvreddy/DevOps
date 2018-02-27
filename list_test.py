l1=[11,12,13,14,17,19,24,26]
l,le,lo = [],[],[]
for i in l1:
    if i%2 == 0:
        le.append(i)
    else:
        lo.append(i)
print le,lo

for i in range(len(lo)):
    l.append(lo[i])
    l.append(le[i])
    
print l
