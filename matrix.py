M = [[1,2,3],[4,5,6],[7,8,9]]
l=[]
k=3
for i in range(0,k):
    for j in range(0,k):
        if i%2 <> 0:
            l.append(M[i][k-1-j])
        else:
            l.append(M[i][j])
        #print l

print l


#o/p: [1, 2, 3, 6, 5, 4, 7, 8, 9]
