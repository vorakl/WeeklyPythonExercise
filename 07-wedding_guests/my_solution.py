#!/usr/bin/env python3

from collections import defaultdict

class TableFull(Exception):
    pass

class Person:
    
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

    def get_name(self):
        ''' Returns: a tuple of the First and Last names
        '''
        return (self.first_name, self.last_name)


class GuestList:

    _max_guests_table = 10

    def __init__(self):
        # contains guests' names (a tuple of First and Last names) as a key for
        # faster searching. Values are tuples of a person object and a table
        self._guests = dict()
        # contains table's assignments, where a table number is a key
        # and values are lists with person objects
        self._tables = defaultdict(list)

    # person here is an object. To ensurethat we do not create a new
    # object for the same name every time, _guests dictionary is used to
    # maintain a connection bwtween unique names and its corresponding object
    def assign(self, person, table):
        # ensure that it gets a person object
        if not isinstance(person, Person):
            raise TypeError(f"A wrong type of the argument: {type(person)}")

        # if not assigned, use a table number 0
        if table is None:
            table = 0

        # if there are more than _max_guests_table people assigned to a table
        if len(self._tables[table]) >= GuestList._max_guests_table:
            raise TableFull(f"The table {table} has 10 assigned people already")

        # if it's a new person (based on the person's full name)
        person_name = person.get_name()
        if person_name not in self._guests:
            self._guests[person_name] = (person, table)
            self._tables[table].append(person)
        else:
            # a person exists
            exist_person, exist_table = self._guests[person_name]
            # assign a person to a new tabel
            if exist_table != table:
                self._tables[exist_table].remove(exist_person)
                self._guests[person_name] = (exist_person, table)
                self._tables[table].append(exist_person)
            else:
                # thesame person, the same table. Do nothing
                pass

    def __len__(self):
        return sum([len(v) for v in self._tables.values()])

    def table(self, number):
        return self._tables[number]

    def unassigned(self):
        return self._tables[0]

    def free_space(self):
        return {k: (GuestList._max_guests_table - len(l))
                for k, l in self._tables.items() if k != 0}

    def guests(self):
        return sorted([(int(self._guests[(fn, ln)][1]), ln, fn)
                       for fn, ln in self._guests])

    def __str__(self):
        prev_tbl = 0
        res = ''
        for tbl, ln, fn in self.guests():
            if tbl == 0:
                continue

            if tbl != prev_tbl:
                res += f'{tbl}:\n'
            else:
                res += f'\t{ln}, {fn}\n'

            prev_tbl = tbl

        return res


def main():
    gl = GuestList()

    gl.assign(Person('Waylon', 'Dalton'), 1)
    gl.assign(Person('Justine', 'Henderson'), 1)
    gl.assign(Person('Abdullah', 'Lang'), 3)
    gl.assign(Person('Marcus', 'Cruz'), 1)
    gl.assign(Person('Thalia', 'Cobb'), 2)
    gl.assign(Person('Mathias', 'Little'), 2)
    gl.assign(Person('Eddie', 'Randolph'), None)
    gl.assign(Person('Angela', 'Walker'), 2)
    gl.assign(Person('Lia', 'Shelton'), 3)
    gl.assign(Person('Hadassah', 'Hartman'), None)
    gl.assign(Person('Joanna', 'Shaffer'), 3)
    gl.assign(Person('Jonathon', 'Sheppard'), 2)
    
    print(f'Total guests: {len(gl)}')
    print(f'Table 2: {gl.table(2)}')
    print(f'Unassigned: {gl.unassigned()}')
    print(f'Free space: {gl.free_space()}')
    print(gl)

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
