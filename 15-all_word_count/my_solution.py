#!/usr/bin/env python3

from glob import glob
from queue import Queue
from timeit import timeit
import threading


def count_words_sync(mask):

    def file_words(fn):
        return sum([len(l.split()) for l in open(fn).readlines()])

    return sum([file_words(b) for b in glob(mask)])


def count_words_async(mask):

    def file_words(fn):
        res = 0
        with open(fn) as f:
            for l in f:
                res += len(l.split())
        q.put(res)


    q = Queue()
    res = 0

    for g in glob(mask):
        threading.Thread(target=file_words, args=(g,)).start()

    while threading.active_count() > 1:
        for t in threading.enumerate():
            if t == threading.current_thread():
                continue


    while not q.empty():
        res += q.get()

    return res

print(timeit(stmt='print(count_words_sync("*.txt"))', number=1, globals=globals()))
print(timeit(stmt='print(count_words_async("*.txt"))', number=1, globals=globals()))

