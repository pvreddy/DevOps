n=int(raw_input('enter number: '))
def fact(n):
      f=1
      if n<2:
          return f  
      else:
          f=n*fact(n-1)
      return f
s=fact(n)
print s
