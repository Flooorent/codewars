#!/usr/bin/python

import string

def mix(s1, s2):
    letter_count_s1 = {letter: 0 for letter in string.ascii_lowercase}
    letter_count_s2 = {letter: 0 for letter in string.ascii_lowercase}

    for letter in s1:
        if letter.isalpha() and letter.islower():
            letter_count_s1[letter] += 1

    for letter in s2:
        if letter.isalpha() and letter.islower():
            letter_count_s2[letter] += 1

    letter_string_max = []

    for letter in string.ascii_lowercase:
        l1 = letter_count_s1[letter]
        l2 = letter_count_s2[letter]

        if (l1 > l2) and (l1 > 1):
            letter_string_max.append((letter, 1, l1))
        elif (l2 > l1) and (l2 > 1):
            letter_string_max.append((letter, 2, l2))
        else:
            if l1 > 1:
                letter_string_max.append((letter, 3, l1))

    letter_string_max.sort(key=lambda t: (-t[2], t[1], t[0]))

    res1 = map(lambda t: (t[0], '=', t[2]) if t[1] == 3 else t, letter_string_max)
    res2 = map(lambda t: str(t[1]) + ':' + t[0]*t[2], res1)
    return '/'.join(res2)

