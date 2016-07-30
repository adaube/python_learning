#!/usr/bin/python

# avoid the 'diamond shape' inheritance (ambiguous)
# happens when inheritance hierarchy leads to same parent in > 1 branch


# example of python lookup tree (depth first)
class A(object):

    def do_this(self):
        print('doing this in A')


class B(A):
    pass

# if C inherits from A, becomes 'diamond shape'
class C(object):

    def do_this(self):
        print('doing this in C')


class D(B,C):
    pass


d_instance = D()

d_instance.do_this()

# method resolution order
print(D.mro())