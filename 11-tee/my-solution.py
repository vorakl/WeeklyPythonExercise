#!/usr/bin/env python3

import sys

class Tee:
    def __init__(self, *args):
        self.fds = args
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        for f in self.fds:
            f.close()

    def write(self, text):
        for f in self.fds:
            f.write(text)

    def writelines(self, lines):
        for f in self.fds:
            f.write(lines)

def main():
    with Tee(sys.stdout,
             open('/tmp/f1.txt', "w"),
             open('/tmp/f2.txt', "w")) as t:
        t.write('abc\n')
        t.write('def\n')
        t.write('ghi\n')

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
