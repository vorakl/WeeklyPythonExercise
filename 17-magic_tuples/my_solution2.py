#!/usr/bin/env python3

class magic_tuples:

    def __init__(self, total, max_val):
        self.total = total
        self.max_val = max_val


    def __iter__(self):
        for i in range(1, self.total // 2 + 1):
            if i < self.max_val and self.total-i < self.max_val:
                yield (i, self.total-i)
                if self.total-i != i:
                    yield (self.total-i, i)
