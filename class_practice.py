class A():
    d = 10
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add1(self):
        print self.x+self.y
    def multi1(self):
        print self.x*self.y
    @staticmethod
    def test1():
        print 'hello'
	
    @classmethod
    def test2(A):
        print 'hello'

class B(A):
    	    
    def sub1(self):
        print self.x - self.y
		
obj = B(10,20)
obj.add1()
obj.sub1()
