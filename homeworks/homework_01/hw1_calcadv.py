#!/usr/bin/env python
# coding: utf-8

def advanced_calculator(input_string):
    input_string = input_string.replace("(", " ( ")
    input_string = input_string.replace(")", " ) ")
    input_string = input_string.replace("+", " + ")
    input_string = input_string.replace("-", " - ")
    input_string = input_string.replace("*", " * ")
    input_string = input_string.replace("/", " / ")
    input_string = " ( " + input_string + " ) "
    input_string = input_string.split()

    stack = []
    output = []
    for i in input_string:
        if i in ("+", "-"):
            if len(stack) > 0:
                while stack[-1] in ("+", "-", "*", "/"):
                    x = stack.pop()
                    output.append(x)
                stack.append(i)
            else:
                return None
        elif i in ("*", "/"):
            if len(stack) > 0:
                while stack[-1] in ("*", "/"):
                    y = stack.pop()
                    output.append(y)
                stack.append(i)
            else:
                return None
        elif i == "(":
            stack.append(i)
        elif i == ")":
            if "(" in stack and stack[-1] != "(":
                stack = stack[::-1]
                k = stack.index("(")
                for j in stack[0:k]:
                    x = stack.pop(stack.index(j))
                    output.append(x)
                stack.remove("(")
                stack = stack[::-1]
            else:
                return None
        elif set(i).issubset(set("0123456789.")):
            output.append(i)
        else:
            return None

    for j in output:
        if j == "+":
            if len(stack) > 1:
                x = stack.pop()
                y = stack.pop()
                stack.append(x + y)
            else:
                return None
        elif j == "-":
            if len(stack) > 1:
                x = stack.pop()
                y = stack.pop()
                stack.append(y - x)
            else:
                return None
        elif j == "*":
            if len(stack) > 1:
                x = stack.pop()
                y = stack.pop()
                stack.append(x * y)
            else:
                return None
        elif j == "/":
            if len(stack) > 1:
                 x = stack.pop()
                 y = stack.pop()
                 stack.append(y // x)
            else:
                return None
        elif set(j).issubset(set("0123456789")) and set(j).issubset(set(".")):
            stack.append(float(j))
        else:
            stack.append(int(j))
    if len(stack) == 0:
        return None
    else:
        return stack.pop()
