#!/usr/bin/python

# brute force
def fisHex(name):
    s = name.lower()
    res = 0

    for c in s:
        if c == 'a':
            res ^= 10
        elif c == 'b':
            res ^= 11
        elif c == 'c':
            res ^= 12
        elif c == 'd':
            res ^= 13
        elif c == 'e':
            res ^= 14
        elif c == 'f':
            res ^= 15
    
    return res

# cleaner way
def fisHex(name):
    hexa = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    s = name.lower()
    res = 0
    for c in s:
        res ^= hexa.get(c, 0)
    return res

# beautiful way, by zebulan
VALID = frozenset("abcdefABCDEF")

def fisHex(name):
    return reduce(lambda b, c: b^c, (int(a, 16) for a in name if a in VALID), 0)

