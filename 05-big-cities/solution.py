#!/usr/bin/env python3

import requests
import csv

URL = 'https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json'
FIELDS = ('city', 'state', 'population', 'rank')

try:
    jres = requests.get(URL).json()
except json.decoder.JSONDecodeError as err:
    raise SystemExit('ERROR: JSON Decode Error: {}'.format(err))

with open('/dev/stdout', 'wt', newline='') as csv_file:
    csvwr = csv.DictWriter(csv_file,
                           fieldnames=FIELDS,
                           delimiter='\t')
    csvwr.writeheader()
    csvwr.writerows([{k:v for k, v in zip(FIELDS, [e[i] for i in FIELDS])}
                          for e in jres])

