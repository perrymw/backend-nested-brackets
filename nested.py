#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: Checks for valid brackets.
"""
__author__ = "perrymw"

import sys

def file_fido(filename):
    """Takes the input text and converts to a list"""
    # +++your code here+++
    with open(filename, 'r') as f:
        text = f.read().split("\n")
    return text

def main(arg):
    count = 0
    stack = []
    bracket = {")": "(", "*)": "(*", "}": "{", ">": "<", "]": "["}
    opening_brackets = bracket.values()
    closing_brackets = bracket.keys()
    listy = list(arg)
    skip_next = False
    for index, token in enumerate(listy):
        if skip_next:
            skip_next = False
            # count += 1 
            continue
        else:
            if index != len(listy)-1:
                if token == "(" and listy[index + 1] == "*":
                    token = "(*"
                    skip_next = True
                elif token == "*" and listy[index + 1] == ")":
                    skip_next = True
                    token = "*)"
            if token in opening_brackets:
                stack.append(token)
                count += 1
            # not stack === len(stack) != 0
            elif token in closing_brackets:
                target_bracket = bracket[token]
                count += 1
                # if stack.index(target_bracket) == len(stack)-1:
                if stack[-1] == target_bracket:
                    stack.pop()
                else:
                    return "No {}".format(count)
            else:
                count += 1
    if len(stack) == 0:
        return "Yes"
    else:
        count += 1
        return "No {}".format(count)

def new_file():
    read_output = file_fido("input.txt")
    with open('output.txt', 'w+') as f:
        for data in read_output:
            content = main(data)
            f.write(content + '\n')

if __name__ == '__main__':
    new_file()
