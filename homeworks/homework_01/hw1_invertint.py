#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    s = str(number)
    if s[0] == "-":
        b = s[1:]
        if b.isdigit():
            s = "-" + b[::-1]
            return int(s)
    else:
        return int(s[::-1])
