#!/usr/bin/env python
# -*- coding: utf-8 -*-


from itertools import count,takewhile,product, permutations

for i in count(3):
    print(i)
    if i>= 11:
        break

nums =[11,22,33,44,55]
print(nums)
print(list(takewhile(lambda x: x<=35,nums)))


letters=("A","B")
print(list(product(letters,range(2))))
print(list(permutations(letters)))
