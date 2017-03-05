#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Pure functions have no side effects, and return a value that depends
#only on their arguments

def pure_function(x,y):
    temp = x + 2*y
    return temp / (2*x +y)

some_list = []

def impure(arg):
    some_list.append(arg)

#Wywołanie
impure(5)
print(some_list)
