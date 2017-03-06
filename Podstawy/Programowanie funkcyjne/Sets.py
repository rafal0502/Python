#!/usr/bin/env python
# -*- coding: utf-8 -*-



#Sets - podobne do słowników i list. Używamy nawiasów klamrowych do ich
#tworzenia. Możemy np użyć wyrażenia "in" jak w lisatch,sprawdzające,czy
#dany element jest w zbiorze.Metody tworzenia:

num_set={1,2,3,4,5}
word_set=set(["spam","eggs","sausage"])

print(3 in num_set)
print("spam" not in word_set)

#By stworzyć pustego seta należy użyć set(), bo puste {} tworzą słownik.

#Nie są indeksowane
#Nie zawierają duplikatów

print("=====================")
nums = {1,2,3,1,4,5,6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

print("=====================")
first = {1,2,3,4,5,6}
second = {4,5,6,7,8,9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)
