#!/usr/bin/env python3

import re
from pprint import pprint as pp

def parse_logfile(fname):
    '''
    :param fname: log file name
    :return: list of dict
    '''

    fields = ('ip_address', 'timestamp', 'request')
    log_ptrn = re.compile(r"""(^\d+\.\d+\.\d+\.\d+)  # IP addr
                                     .+?                    # -
                                     \[(.+?)\]              # timestamp
                                     \s+"                   # -
                                     (.+?)"                 # request
                                     """, re.X)
    res = list()

    with open(fname, "r") as log:
        while line := log.readline():
            logrec = re.match(log_ptrn, line)
            if logrec and len(logrec.groups()) == 3:
                res.append({k:v for k, v in zip(fields, logrec.groups())})

    return res

def main():
    fname = 'mini-access-log.txt'
    flogs = parse_logfile(fname)
    pp(flogs)
    print(f"Total records: {len(flogs)}")

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
