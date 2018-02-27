class A:
    x = 30

class B(A):
    pass

class C(A):
    pass


obj = A
obj1 = B
obj2 = C

obj.x=3
obj1.x = 2
print obj.x
print obj1.x
print obj2.x
