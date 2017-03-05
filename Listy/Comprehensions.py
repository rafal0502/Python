#!/usr/bin/env python
# -*- coding: utf-8 -*-

#a list comprehension

cubes = [i**3 for i in range(5)]

print(cubes)


#wzorzec listowy? może zawierać wyrażenie if by narzucić jakiś warunek w liście

evens = [i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)
