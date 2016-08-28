#!/usr/bin/python

def reverse(c):
    if c == '}':
        return '{'
    elif c == ')':
        return '('
    else:
        return '['

def valid_braces(string):
    """The perfect data structure here is a stack."""
    open = "({["
    stack = []

    for c in string:
        if c in open:
            stack.append(c)
        else:
            if stack and stack[-1] == reverse(c):
                stack.pop()
            else:
                return False

    if stack: # some braces and co. were not closed
        return False
    else:
        return True

