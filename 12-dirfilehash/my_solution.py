#!/usr/bin/env python3

import hashlib
from pathlib import Path
from os.path import join as path_join

class DirFileHash:

    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.file_hash = {k.name: None for k in Path(dir_name).iterdir()} 

    def __getitem__(self, key):
        if key not in self.file_hash:
            return None
        elif self.file_hash[key] is None:
            with open(path_join(self.dir_name, key), "rb") as f:
                self.file_hash[key] = hashlib.file_digest(f, "md5").hexdigest()

        return self.file_hash[key]
            

def main():
    d = DirFileHash(".")
    print(d["some.file"])
    print(d["my_solution.py"])

    return 0

if __name__ == '__main__':
    raise SystemExit(main())

