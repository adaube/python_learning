#!/usr/bin/python


class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = self.filter_int(val)
        InstanceCounter.count += 1

    # requires no argument, does not work with class or instance but
    # still belongs in class code
    @staticmethod
    def filter_int(value):
        if not isinstance(value, int):
            return 0
        else:
            return value

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count


a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter('hello world')

for obj in (a, b, c):
    print('val of obj: {0}'.format(obj.get_val()))
    print('count: {0}'.format(obj.get_count()))
