#!/usr/bin/env python3

class Uniquish:

    def __hash__(self):
        return hash(tuple(self.__dict__.values()))

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return tuple(self.__dict__.values()) == tuple(other.__dict__.values())
        else:
            raise NotImplemented


class Foo(Uniquish):

    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c


class Bar(object):

    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c


f1 = Foo(4, 5, 6)
f2 = Foo(4, 5, 6)
s = {f1, f2}
print(f'{f1 == f2 = }')
print(f'{f1 is f2 = }')
print(f'{hash(f1) = }')
print(f'{hash(f2) = }')
print(f'{s = }')

b1 = Bar(4, 5, 6)
b2 = Bar(4, 5, 6)
s = {b1, b2}
print(f'{b1 == b2 = }')
print(f'{b1 is b2 = }')
print(f'{hash(b1) = }')
print(f'{hash(b2) = }')
print(f'{s = }')
