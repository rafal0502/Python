#!/usr/bin/env python
# -*- coding: utf-8 -*-


#By połączyć nie stringi i stringi wcześniej konwertowaliśmy
# nie stringi do stringów i dodawaliśmy

#Formatowanie stringów dostarcza mocniejszego by "osadzić"
#nie string wewnątrz stringów. Używamy do tego string's format
#method by zastąpić agumenty stringami.

nums = [4,5,6]
msg = "Numbers: {0} {1} {2}".format(nums[0],nums[1],nums[2])
print (msg)

a = "{x},{y}".format(x=5,y=16)
print(a)
