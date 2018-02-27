#def multi_func(l,x):
 #   l2 = [i for i in l if i%x == 0]
  #  return l2



def multi_func(l,x,l2 = None):
    l2 = [ ]
    for i in l:
        if i%x == 0:
            l2.append(i)
    return l2
print multi_func([1,2,3,4,5,6],2.5)
