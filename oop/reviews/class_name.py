class A(object):
    def whoami(self):
        print(type(self).__name__)

class B(A):
    pass

a1 = A()
a1.whoami()
b1 = B()
b1.whoami()
