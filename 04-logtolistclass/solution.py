class LogDicts(object):

    def __init__(self, fname):
        import re

        self.logs = list()
        fields = ('ip_address', 'timestamp', 'request')
        mask = re.compile(r'(\d+\.\d+\.\d+\.\d+).+\[(.+)\]\s+\"(.+?)\"')

        with open(fname, 'rt') as logfile:
            for log in logfile:
                r = mask.search(log.strip())
                if r:
                    self.logs.append({k:v for k, v in zip(fields, r.groups())})

    def dicts(self, key=None):
        if key:
            return sorted(self.logs, key=key)
        return self.logs

    def iterdicts(self, key=None):
        if key:
            return iter(sorted(self.logs, key=key))
        return iter(self.logs)

    def for_ip(self, ip_addr, key=None):
        res = [log for log in self.logs if log['ip_address'] == ip_addr] 
        if key:
            return iter(sorted(res, key=key))
        return res

    def for_request(self, req, key=None):
        res = [log for log in self.logs if log['request'].find(req) != -1]
        if key:
            return iter(sorted(res, key=key))
        return res 

    def earliest(self):
        import time
        return sorted(self.logs,
                      key=lambda x: time.strptime(x['timestamp'],
                                                  '%d/%b/%Y:%H:%M:%S %z'))[0]

    def latest(self):
        import time
        return sorted(self.logs, 
                      key=lambda x: time.strptime(x['timestamp'],
                                                  '%d/%b/%Y:%H:%M:%S %z'))[-1]

