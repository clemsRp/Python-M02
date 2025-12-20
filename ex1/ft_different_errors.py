#!/usr/bin/env python3

def garden_operations():
    print(int("abc"))
    print(10 / 0)
    with open("missing.txt", "r") as f:
        print(f.read())
    alphabet = {"voyelles": 6, "consonnes": 20}
    print(alphabet["majuscules"])


def test_error_types():
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        num = int("abc")
    except ValueError as e:
        print("Caught ValueError:", e, "\n")

    print("Testing ZeroDivisionError...")
    try:
        num = 10 / 0
        print(num)
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e, "\n")

    print("Testing FileNotFoundError...")
    try:
        with open("missing.txt", "r") as f:
            print(f.read())
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e, "\n")

    print("Testing KeyError...")
    try:
        alphabet = {"voyelles": 6, "consonnes": 20}
        nb_maj = alphabet["majuscules"]
        print(nb_maj)
    except KeyError as e:
        print("Caught KeyError:", e, "\n")

    print("Testing multiple errors together...")
    try:
        int("abc")
        num = 10 / 0
        print(num)
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
