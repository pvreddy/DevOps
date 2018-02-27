# we need to print the second highest repeated word in a file.

def second_highest(filename):
    f = open(filename,'r')
    d = {}
    lines = f.readlines()
    #print lines
    for line in lines:
        words = line.split(" ")
        for word in words:
            if d.has_key(word):
                d[word] = d[word] + 1
            else:
                d[word] = 1
    
    return sorted(d.iteritems(), key = lambda x:x[1],reverse = True)[1]

print second_highest('test.txt')
        
        
