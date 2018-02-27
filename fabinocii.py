x = int(raw_input('enter value: '))

def febonocii2(x):
    a,b = 0,1
    while b<x:
        a,b = b,a+b
        print a

s = febonocii2(x)
