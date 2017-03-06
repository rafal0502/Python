#!/usr/bin/env python
# -*- coding: utf-8 -*-

#map używamy z agrumentem list (albo innym typu iterable) by przejść po
#każdym

def add_five(x):
    return x + 5

nums = [11,22,33,44,55]
result = list(map(add_five,nums))
print(result)


#z lambdą

result = list(map(lambda x: x+5,nums))
print(result)

