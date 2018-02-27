

def fib(n):
    result = []
    n = int(n)
    a,b = 0,1
    while b < n:
        result.append(b)
        a,b = b, a+b
    return result
        

n = raw_input('Enter value of n : ')
print fib(n)
