

def hrml(m,n):
    print m + "  " + n
    x = m/2
    for i in range(1,x+1):
        print "<tag" + str(i)+ " "+ "value = 'helloworld'>"
        print "<\tag" + str(i)+">"
    for j in range(n):
        
        

m = raw_input('enter m value : ')
n = raw_input('enter n value : ')

hrml(m,n)

    
