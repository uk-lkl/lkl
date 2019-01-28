#!/usr/bin/env python

import sys

for line in sys.stdin:
    toks = line[:-1].split(" ")
    if len(toks) != 3:
        continue
    if toks[1] == "T" or toks[1] == "D" or toks[1] == "B":
        print(toks[2])
