#!/usr/bin/env python3

from collections import defaultdict, Counter

travel_db = defaultdict(list)

def get_travels(db):
    while True:
        s = input('Tell me where you went: ')
        if not s:
            break
        elif s.find(',') == -1:
            print("That's not a legal city, state combination")
        else:
            city, country = s.split(',', 1)
            db[country.strip(' ')].append(city.strip(' '))

def print_report(db):
    for country in sorted(db.keys()):
        print(f'{country}')
        cities = Counter(sorted(db[country]))
        for c in cities:
            if cities[c] > 1:
                print(f'\t{c} ({cities[c]})')
            else:
                print(f'\t{c}')

get_travels(travel_db)
print_report(travel_db)
