n = int(raw_input('enter n value : '))
def fib(n):
    result = []
    x,y = 0,1
    while y<n:
        result.append(y)
        x,y = y,x+y
    print result

fib(n)
