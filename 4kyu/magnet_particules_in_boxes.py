#!/usr/bin/python

# the trick was to apply the power to the fraction directly and not to the quotient 
def doubles(maxk, maxn):
    res = 0.0
    for k in xrange(1, maxk+1):
        for n in xrange(1, maxn+1):
            res += pow(1.0/(n+1), 2.0*k)*1.0/k
    return res
