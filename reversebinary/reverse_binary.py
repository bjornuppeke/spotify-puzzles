#!/usr/bin/env python

import sys

def reverse_binary(n):
	"""Return int of a the reversed binary representation of `n`

	>>> reverse_binary(13)
	11

	"""

	return int(bin(n)[:1:-1], 2)

if __name__ == "__main__":
    for line in sys.stdin:
        try:
            n = int(line)
            print reverse_binary(n)
        except ValueError, e:
            sys.stderr.write("Invalid input.\n")
