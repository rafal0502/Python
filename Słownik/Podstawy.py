#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Each element in a dictionary is represented by key:value pair.

ages = {"Dave" :24, "Mary":42, "John":58}
print(ages["Dave"])
print(ages["John"])


#Dodanie nowego klucza i wartości - nie trzeba definiować w słowniku od razu
squares = {1:1,2:4,3:"error",4:16,} #przecinek na końcu?
squares [8] = 64
squares[3] = 9  #redefinicja

print(squares)

#in not in - czy klucz jest w słowniku
nums = {1:"one",2:"two",3:"three",}
print (1 in nums)
print ("three" in nums)
print (4 not in nums)
