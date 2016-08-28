#!/usr/bin/python

def order_weight(strng):
    if strng == "":
        return ""

    weights = strng.strip().split(' ')
    both_weights = [[w, sum(map(int, list(w)))] for w in weights]
    sorted_weights = sorted(both_weights, key=lambda elem: (elem[1], elem[0]))
    return ' '.join(map(lambda elem: elem[0], sorted_weights))

