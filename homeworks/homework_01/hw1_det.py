#!/usr/bin/env python
# coding: utf-8
import copy


def find_minors(list_of_lists, i, j):
    matrix = copy.deepcopy(list_of_lists)
    del matrix[i]
    for i in range(len(list_of_lists[0]) - 1):
        del matrix[i][j]
    return matrix


def calculate_determinant(list_of_lists):
    sign = 1
    determinant = 0
    x = len(list_of_lists)
    y = len(list_of_lists[0])
    if x != y:
        return None
    if y == 1:
        return list_of_lists[0][0]
    for j in range(y):
        determinant += list_of_lists[0][j] * sign * calculate_determinant(find_minors(list_of_lists, 0, j))
        sign *= -1
    return determinant
