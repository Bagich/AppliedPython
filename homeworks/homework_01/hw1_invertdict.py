#!/usr/bin/env python
# coding: utf-8

def extract(v, t):
    if isinstance(v, set) or isinstance(v, tuple) or isinstance(v, list):
        for i in v:
            splitvals(i, t)
    else:
        t.append(v)


def invert_dict(source_dict):
    tmp_dict = dict()
    new_dict = dict()
    if source_dict:
        for k, v in source_dict.items():
            arr = []
            extract(v, arr)
            tmp_dict[k] = arr
        for k, v in tmp_dict.items():
            for l in v:
                if l not in new_dict.keys():
                    new_dict[l] = k
                else:
                    if not isinstance(new_dict[l], list):
                        new_dict[l] = [new_dict[l]]
                    new_dict[l].append(k)
    return new_dict
