#!/usr/bin/env python3

from random import randint

class RandMemory:

    def __init__(self, l, r):
        self.rand_range = (l, r)
        self.rand_memory = []

    @property
    def get(self):
        self.rand_memory.append(randint(*self.rand_range))
        return self.rand_memory[-1]

            
    def history(self):
        return self.rand_memory


def main():
    r = RandMemory(1,100)
    print(r.get)
    print(r.get)
    print(r.get)
    print(r.get)
    print(*r.history())

    return 0


if __name__ == '__main__':
    raise SystemExit(main())

