#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python za pomocą pewnych wyrażeń pozwala nam
zdefiniować jednolinijkowe mini-funkcje.
>>> def f(x):
...     return x*2
...
>>> f(3)
6
>>> g = lambda x: x*2      #(1)   to samo co wyżej, przypisanie do zm. g
>>> g(3)
6
>>> (lambda x: x*2)(3)     #(2)
6
"""

#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x +4)(-4))
