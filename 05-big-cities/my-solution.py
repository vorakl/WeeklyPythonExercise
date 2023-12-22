#!/usr/bin/env python3

import requests
import csv
from sys import stderr

url = ("https://gist.githubusercontent.com/reuven/"
       "77edbb0292901f35019f17edb9794358/raw/"
       "2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json")


def print_tb():
    """Prints a Stack Trace"""
    tb = format_exc().splitlines()
    tb_err = tb[-1]
    tb_stack = "\\n".join(tb[:-1])
    print(f"[ERROR, unhandled] {tb_err}", file=stderr, flush=True)
    print(f"[ERROR, unhandled] {tb_stack}", file=stderr, flush=True)


def write_csv(file_name, json_doc):
    fields = ["city", "state", "population", "rank"]
    with open(file_name, "wt", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file,
                                    fieldnames=fields,
                                    delimiter="\t",
                                    extrasaction='ignore')
        csv_writer.writeheader()
        csv_writer.writerows(json_doc)


def main():
    try:
        res = requests.get(url, timeout=5)
    except Exception:
        print_tb()
        raise SystemExit(1)

    write_csv("big_cities.csv", res.json())


if __name__ == "__main__":
    main()
