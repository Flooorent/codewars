#!/usr/bin/python

def loop_size(node):
    """
    First make sure you arrive at a node that is in the loop.
    Then from there simply loop to get the length of the loop.
    """
    if not node:
        return 0

    slow = node
    fast = node.next
    
    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    fast = fast.next
    length = 1
    while slow != fast:
        fast = fast.next
        length += 1

    return length

