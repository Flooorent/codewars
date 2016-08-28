#!/usr/bin/python

import math

def race(v1, v2, g):
    """
    We want to find the first second where turtoise B is at the same level or ahead
    of turtoise A. To do this we simply need to calculate the gap between the two at
    each second and pick the time when that gap becomes negative or zero.
    
    At second k, the gap is: g_k = g - k*(v2-v1)/3600, so we are looking for the first
    k such that g - k*(v2-v1)/3600 <= 0 ie k >= 3600*g/(v2-v1).

    Since we don't have to worry for fractions of second, the answer is:
    k = math.floor(3600*g/(v2-v1))
    """
    if v2 <= v1:
        return None

    time = math.floor(3600 * g / (v2-v1))
    hours = math.floor(time / 3600)
    minutes = math.floor((time - hours*3600) / 60)
    seconds = time - hours*3600 - minutes*60

    return [hours, minutes, seconds]

# smarter way by 3rogue
def race(v1, v2, g):
    if v1 >+ v2:
        return None
    res = g*3600/(v2-v1)
    return [res / 3600, res % 3600 / 60, res % 60]

