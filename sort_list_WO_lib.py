l = [2,4,1,5,9,7,13,3]
li=[]
for x in xrange(0,len(l)-1):
    print l[x]
    if l[x]<l[x+1] and l[x+1]>l[x+2]:
        li.append(l[x+1])
    else:
        continue


print li
    
        
