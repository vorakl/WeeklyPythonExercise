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

    line_count = 0

    while opts.file.readline():
        line_count +=1
    opts.file.seek(0)

    # ensure we don't try to print more lines than exist
    opts.start, opts.end = map(validate(line_count), (opts.start, opts.end))

    target_line = line_count - opts.end
    print(f'{line_count = }, {target_line = }')

    print('\nHead:')
    i = 0
    while l := opts.file.readline():
        if i < opts.start:
            print(f'{l.rstrip()}')
        elif i == opts.start:
            print('\nTail:')
        elif i >= target_line:
            print(f'{l.rstrip()}')
        else:
            pass

        i += 1


def main():
    opts = parse_cli()
    print_head_tail(opts)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())


