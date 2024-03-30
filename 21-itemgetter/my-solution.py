#!/usr/bin/env python3

def itemgetter(*args):

    def helper(data):
        if len(args) == 1:
            return getattr(data, '__getitem__')(args[0])
        else:
            return tuple((getattr(data, '__getitem__')(i) for i in args))

    return helper


mygetter1 = itemgetter(1)
print(mygetter1([1,2,3]))

mygetter2 = itemgetter(1,2)
print(mygetter2("asd"))

mygetter3 = itemgetter('b')
print(mygetter3({'a':1, 'b':2}))

mygetter4 = itemgetter('a', 'b')
print(mygetter4({'a':1, 'b':2}))
