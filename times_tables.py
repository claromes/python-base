#!/usr/bin/env python3
"""Print times table 1 to 10."""
__version__ = "0.1.1"
__author__  = "claromes"

numbers = list(range(1, 11))

print("{:^23}".format("times tables\n".upper()))

for number_1 in numbers:
    print("{:^23}".format(f"{number_1} Times Table \N{Abacus}\n"))

    for number_2 in numbers:
        result = number_1 * number_2
        print("{:^23}".format(f"{number_1} x {number_2} = {result}"))

    print("." * 23)