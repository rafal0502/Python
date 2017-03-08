#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Metacharacters to to, co sprawia,że wyr. regualrne sa potezniejsze
#od stringow. Pomagaja wytwarzac wyrazenia jak 'powtarzanie samogloski

#First metacharacter  we will look at is .(dot)
#Dopasowuje dowolnu nzak inny niz nowej linii

import re

pattern = r"gr.....y"

if re.match(pattern,"grey"):
    print("Match 1")

if re.match(pattern, "grafewfy"):
    print("Match 2")

if re.match(pattern, "blue"):
    print("Match 3")




