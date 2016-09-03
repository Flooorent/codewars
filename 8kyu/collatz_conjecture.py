#!/usr/bin/python

def hotpo(n):
    count = 0
    temp = n
    while temp != 1:
        if temp % 2 == 0:
            temp /= 2
        else:
            temp = 3*temp + 1
        count += 1
    return count

