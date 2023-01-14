#!/usr/bin/env python3

"""Simple fizzbuzz generator.

This script prints out a sequence of numbers from a provided range
with the following restrictions:

- if the number is divisible by 3, then print out "fizz",
- if the number is divisible by 5, then print out "buzz",
- if the number is divisible by 3 and 5, then print out "fizzbuzz".
"""

import argparse
import sys


class CustomFormatter(argparse.RawDescriptionHelpFormatter,
                      argparse.ArgumentDefaultsHelpFormatter):
    pass


def parse_args(args=sys.argv[1:]):
    """Parse arguments"""
    parser = argparse.ArgumentParser(
        description=sys.modules[__name__].__doc__,
        formatter_class=CustomFormatter)


    g = parser.add_argument_group("fizzbuzz settings")
    g.add_argument("--fizz", metavar="N",
                   default=3,
                   type=int,
                   help="Modulo value for fizz")
    g.add_argument("--buzz", metavar="N",
                   default=5,
                   type=int,
                   help="Modulo value for buzz")

    parser.add_argument("start", type=int, help="Start value")
    parser.add_argument("end", type=int, help="End value")

    return parser.parse_args(args)


options = parse_args()
for n in range(options.start, options.end + 1):
# ...


for n in range(int(sys.argv[1]), int(sys.argv[2])):
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)
