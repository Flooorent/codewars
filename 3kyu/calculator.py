#!/usr/bin/python

class Calculator(object):
    def evaluate(self, string):
        expr = string.strip().split(" ")

        def eval(x, string):
            if not string:
                return x
            elif string[0] == "*":
                return eval(x * float(string[1]), string[2:])
            elif string[0] == "/":
                return eval(x / float(string[1]), string[2:])
            elif string[0] == "+":
                return x + eval(float(string[1]), string[2:])
            else:
                return x + eval(-float(string[1]), string[2:])
        
        return 0 if not expr else round(eval(float(expr[0]), expt[1:]), 3)

