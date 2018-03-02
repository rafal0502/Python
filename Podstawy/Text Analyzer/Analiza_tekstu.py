#!/usr/bin/env python
# -*- coding: utf-8 -*-

def count_char(text,char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

#Input nie działa w atomie

filename = input("Enter a filename: ")
with open(filename) as f:
    tekst_z_pliku = f.read()

print(count_char(tekst_z_pliku,"r"))


#Zawartość procentowa każdej litery

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(tekst_z_pliku,char)/len(tekst_z_pliku)
    print("{0}-{1}%".format(char,round(perc,2)))
