#!/usr/bin/env python3
"""Print times table 1 to 10."""
__version__ = "0.1.0"
__author__  = "claromes"

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(range(1, 11))

# Iterable
for number in numbers:
	print(number, "Times table")
	for other_number in numbers:
	    print(number * other_number)
	print("--------")