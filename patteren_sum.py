"""n = 2
m = 5


pattern : 2 + 22 + 222 + 2222 + 22222
output : 24690

a =12
b =3

patteren : 12 + 1212 + 121212"""


def pat_sum(n,m):
    l = []
    n = str(n)
    for i in range(1,m+1):
        l.append(n*i)
    print l
    
    print "paateren : ", "+".join(l)
    print "output : ", reduce(lambda x,y:int(x) + int(y), l)

pat_sum(12,5)
