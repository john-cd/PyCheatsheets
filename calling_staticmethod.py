
class A(object):
    
    def __init__(self):
        self.stat()   
        A.stat()
        self.f()    
    
    @staticmethod
    def stat():
        print "static method"
    
    def f(self):
        print "f"
        
a = A()
        