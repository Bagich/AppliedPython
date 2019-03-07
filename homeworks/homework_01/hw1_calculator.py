#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if isinstance(x, (float, int)) and isinstance(y, (float, int)):
        if operator == "plus":
            return x + y
        elif operator == "minus":
            return x - y
        elif operator == "mult":
            return x * y
        elif operator == "divide":
            if y == 0:
                return None
            else:
                return x / y
    else:
        return None  

