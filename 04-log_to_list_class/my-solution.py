#!/usr/bin/env python3

import re
import time
from pprint import pprint as pp

class LogDicts():
    def __init__(self, fname):
        self._logs = list()
        self.file_name = fname
        self.parse_logfile()

    def parse_logfile(self):
        fields = ('ip_address', 'timestamp', 'request')
        log_ptrn = re.compile(r"""(^\d+\.\d+\.\d+\.\d+)  # IP addr
                                         .+?                    # -
                                         \[(.+?)]               # timestamp
                                         \s+"                   # -
                                         (.+?)"                 # request
                                         """, re.X)

        with open(self.file_name, "r") as log:
            while line := log.readline():
                logrec = re.match(log_ptrn, line)
                if logrec and len(logrec.groups()) == 3:
                    self._logs.append({k: v for k, v in zip(fields,
                                                            logrec.groups())})

    def iterdicts(self, key=None):
        if key:
            yield from sorted(self._logs, key=key)
        else:
            yield from self._logs

    def dicts(self, key=None):
        return list(self.iterdicts(key))

    def earliest(self):
        return min(self._logs, key=lambda x: time.strptime(x['timestamp'],
                                       '%d/%b/%Y:%H:%M:%S %z'))

    def latest(self):
        return max(self._logs, key=lambda x: time.strptime(x['timestamp'],
                                       '%d/%b/%Y:%H:%M:%S %z'))

    def for_ip(self, ip_address, key=None):
        loc_logs = [i for i in self._logs if i['ip_address'] == ip_address]
        if key:
            return sorted(loc_logs, key=key)
        else:
            return loc_logs

    def for_request(self, text, key=None):
        loc_logs = [i for i in self._logs if re.search(text, i['request'])]
        if key:
            return sorted(loc_logs, key=key)
        else:
            return loc_logs

def main():
    ld = LogDicts('mini-access-log.txt')
    pp(list(ld.dicts(key=lambda x: x['request'].split()[1])))
    print()
    print(ld.earliest())
    print()
    print(ld.latest())
    print()
    pp(ld.for_ip('65.55.215.75',
                 key=lambda x: x['request'].split()[1]))
    print()
    pp(ld.for_request('list_models'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
