#!/usr/bin/env python3


def str_range(start, end, step=1):
    return (chr(i) for i in range(ord(start), ord(end), step))
