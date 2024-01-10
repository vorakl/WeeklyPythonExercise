#!/usr/bin/env python3

import pathlib
from pprint import pprint as pp

def f_len(fn):
    return pathlib.Path(fn).stat().st_size

def filefunc(dir_name, func):
    res = dict()
    err = dict()

    directory = pathlib.Path(dir_name)
    # de Morgan Law: !(a and b) == !a or !b
    if not directory.exists() or  not directory.is_dir():
        raise SystemExit(f"Directory {dir_name} does not exist")

    for f in pathlib.Path(dir_name).iterdir():
        try:
            res[f.absolute()] = func(f.absolute())
        except Exception as exc:
            err[f.absolute()] = exc

    return res, err

def main():
    res, err = filefunc('/etc', f_len)

    pp(res)
    pp(err)

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
