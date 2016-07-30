#!/usr/bin/python

import abc

# abstract classes can define an interface

# can be subclassed by regular classes, but not designed to construct
class GetterSetter(object):
    __metaclass__ = abc.ABCMeta

    # these methods must be implemented by its subclasses
    @abc.abstractmethod
    def set_val(self, input):
        """Set a value in the instance."""
        return

    @abc.abstractmethod
    def get_val(self):
        """Get and return a value from the instance."""
        return

# using abstract class for a "model" of defining our subclass
class MyClass(GetterSetter):

    def set_val(self, input):
        self.val = input

    def get_val(self):
        return self.val

x = MyClass()
print(x)
