#!/usr/bin/env python
# -*- coding: utf-8 -*-

squares = [0,1,4,9,16,25,36,64,81]

print(squares[2:6])
print(squares[0:1])
print(squares[3::8])

#pierwszy argument sie zawiera w rezultacie a drugi nie - jak w RANGE

print(squares[:7])
#od początku
print(squares[7:])
#do konca

#listy moga miec trzeci agrument -step

print(squares[::2])
print(squares[2:8:3])
