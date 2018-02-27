#s(n) = 1.3 + 3.5 + 5.7 + ...... nterms and we need to conider (.) as *
#e.g.: s(0) = 0, s(1) = 3, s(2) = 18

def S(n):
    num = 1
    val = 0
          
    if n < 1:
        return 0
    for i in range(1,n+1):
        val = val + (num * (num+2))
        num  = num + 2 
    return val


print S(5)
