from pprint import pprint as pp

def logtolist(fname):
    import re

    logs = list()
    fields = ('ip_address', 'timestamp', 'request')
    mask = re.compile(r'(\d+\.\d+\.\d+\.\d+).+\[(.+)\]\s+\"(.+?)\"')

    with open(fname, 'rt') as logfile:
        for log in logfile:
            res = mask.search(log.strip())
            if res:
                logs.append({k:v for k, v in zip(fields, res.groups())})
    return logs

pp(logtolist('mini-access-log.txt'))
