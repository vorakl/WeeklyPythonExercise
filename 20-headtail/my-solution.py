#!/usr/bin/env python3


import argparse
import sys

def parse_cli():
    cli = argparse.ArgumentParser(
                    prog='headtail',
                    description=f'Prints a defined number of lines from '
                                f'the beginning and the end of a file.',
                    epilog=f'Example: {sys.argv[0]} -f file')
    cli.add_argument('-s', '--start', metavar='line(s)', type=int, default=3,
                     help='indicating how many lines to show from the start (default = 3)')
    cli.add_argument('-e', '--end', metavar='line(s)', type=int, default=3,
                     help='indicating how many lines to show from the end (default = 3)')
    cli.add_argument('-f', '--file', metavar='name', type=argparse.FileType("r"), required=True,
                     help='indicating the name of the file we want to display the start end of')

    return cli.parse_args()


def print_head_tail(opts):

    def validate(val_max):
        def helper(val):
            return val if val <= val_max else val_max
        return helper

    text = opts.file.readlines()

    # ensure we don't try to print more lines than exist
    opts.start, opts.end = map(validate(len(text)), (opts.start, opts.end))

    head = "\n".join(map(str.rstrip, text[:opts.start]))
    tail = "\n".join(map(str.rstrip, text[-opts.end:]))
    print(f'Head:\n{head}\n')
    print(f'Tail:\n{tail}')


def main():
    opts = parse_cli()
    print_head_tail(opts)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())


