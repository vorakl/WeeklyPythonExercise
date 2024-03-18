#!/usr/bin/env python3

class ThresholdEqual(int):

    def __new__(cls, x, threshold):
        obj = super().__new__(cls, x)
        obj.threshold = threshold
        return obj

    def __repr__(self):
        return f'ThresholdEqual({self})'

    def __eq__(self, ref):
        return True if abs(self - ref) <= self.threshold else False
