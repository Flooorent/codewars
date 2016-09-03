#!/usr/bin/python

def is_opposite(dir1, dir2):
    def get_number(dir):
        if dir == "NORTH":
            return 1
        elif dir == "SOUTH":
            return -1
        elif dir == "WEST":
            return 2
        else:
            return -2
    
    res = get_number(dir1) + get_number(dir2)
    return True if res == 0 else False


def dirReduc(arr):
    new_dir = []
    for dir in arr:
        if not new_dir:
            new_dir.append(dir)
        elif is_opposite(new_dir[-1], dir):
            new_dir.pop()
        else:
            new_dir.append(dir)
    
    return new_dir

# cleaner way by Unnamed
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(arr):
    new_dir = []
    for d in arr:
        if new_dir and new_dir[-1] == opposite[d]:
            new_dir.pop()
        else:
            new_dir.append(d)
    return new_dir

