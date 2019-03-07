#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    ht = {}
    counter = 0
    for v in input_list:
        ad = n - v
        if ad in ht.values():
            for k in ht.keys():
                if ht[k] == ad:
                    return k, counter
        else:
            ht[counter] = v
        counter += 1
    return None
