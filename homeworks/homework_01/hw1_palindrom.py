#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    input_string = input_string.replace(" ", "a")
    if input_string.isalnum():
        for i in range(0, len(input_string)//2, 1):
            if input_string[i] == input_string[-i-1]:
                continue
            else:
                return False
        return True
    else:
        return False
