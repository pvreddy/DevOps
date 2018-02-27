class A:
    def __init__(self):
        self.i=10
    def z(self,g=20):
        return g
        
class B(A):
    def C(self):
        b = self.z
        return b
obj = B()
print obj.C()


