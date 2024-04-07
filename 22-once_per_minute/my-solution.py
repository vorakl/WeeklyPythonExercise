#!/usr/bin/env python3

from functools import wraps
import time

class TooSoonError(Exception):
     pass

def once_per_minute(func):

    @wraps(func)
    def helper(*args, **kwargs):
        nonlocal curr_time

        time_wait = 60 - (time.time() - curr_time)
        if time_wait >= 0:
            raise TooSoonError(f'Wait another {time_wait} seconds')
        else:
            curr_time = time.time()
            return func(*args, **kwargs)

    curr_time = time.time()

    return helper


@once_per_minute
def hello(name):
    return "Hello, {}".format(name)

for i in range(30):
    print(i)
    try:
        time.sleep(3)
        print(hello("attempt {}".format(i)))
    except TooSoonError as e:
        print("Too soon: {}".format(e))
