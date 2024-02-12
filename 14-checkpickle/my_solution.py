#!/usr/bin/env python3

import time
import pickle
import pathlib


INPUT_CHOICES = "qlar"
INPUT_QUIT = "q"
OUTPUT_STEM = "checkpoint"

phone_book = []


def main():
    choice = "-"

    while choice != INPUT_QUIT:
        choice = print_menu()

        match choice:
            case "q":  act_q()
            case "l":  act_l()
            case "a":  act_a()
            case "r":  act_r()
            case _:    pass

    return 0


def act_q():
    print("\nGood Bye!")


def act_l():
    print("\nList people:")
    for pb in phone_book:
        print("{" + f"'first_name': '{pb['first_name']}', "
              f"'last_name': '{pb['last_name']}', "
              f"'email': '{pb['email']}'" + "}")


def act_a():
    print("\nAdd a person")
    fn = input("Enter a first name: ")
    ln = input("Enter a last name: ")
    em = input("Enter an email: ")
    phone_book.append({'first_name': fn, 'last_name': ln, 'email': em})

    with open(f'{OUTPUT_STEM}-{time.strftime("%Y%m%dT%H%M%S")}', "wb") as f:
        pickle.dump(phone_book, f)


def act_r():
    print("\nRestore from a checkpoint.\nList of checkpoints:")
    
    for f in pathlib.Path().iterdir():
        if f.name.find(OUTPUT_STEM) != -1:
            print(f"\t{f.name}")

    checkpoint = input("Enter a file name of the checkpoint: ")
    try:
        with open(checkpoint, "br") as f:
            global phone_book
            phone_book = pickle.load(f)
    except FileNotFoundError as err:
        print(f"[ERROR]: {err}")


def print_menu() -> str:
    choices = INPUT_CHOICES
    keep_asking = True

    while keep_asking:
        print(f"\nMenu:\n"
              f"[q]\tquit\n"
              f"[l]\tlist people\n"
              f"[a]\tadd a person\n"
              f"[r]\trestore a checkpoint\n")
        res = input("Enter: ")
        if res not in choices:
            print("\n[ERROR]: wrong choise!\n")
        else:
            keep_asking = False

    return res


if __name__ == '__main__':
    raise SystemExit(main())

