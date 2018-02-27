global x,y,z

def A(x=1,y=2,z=3):
    x,y,z = 1,2,3
def B(A):
    print x,y,z


A()
B()
