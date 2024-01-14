#!/usr/bin/env python3

letters ='abcde'
numbers = [1,2,3,4,5]
symbols = '!@#$%'

def multiziperator(*keys):
    return (i for k in zip(*keys) for i in k)
        

def main():
    for i in multiziperator(letters, numbers, symbols):
        print(i)

    return 0

if __name__ == '__main__':
    raise SystemExit(main())

