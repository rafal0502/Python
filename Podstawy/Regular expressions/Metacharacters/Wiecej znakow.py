#Znaki ? * + {and} licza ? liczba powtorzen
#* means (zero or more repetitions of the previous thing)
#previous thing can be a single character, a class or a group
#of characters in parentheses

import re

pattern =r"egg(spam)*"

#Przyklad wyzej - 'szukaja' stringow ktore zaczynaja sie od egg
#i po nim nastepuje 0 lub wiecej 'spam'sow

if re.match(pattern,"egg"):
    print 'Match 1'

if re.match(pattern,"eggspamspamegg"):
    print 'Match 2'

if re.match(pattern,"spam"):
    print 'Match 3'

# + podobne do * ale oznacza 1 lub wiecej powtorzen

pattern2 =r"g+"

if re.match(pattern,"g"):
    print "Match 1"

if re.match(pattern,"ggggggggggggggg"):
    print "Match 2"

if re.match(pattern,"abc"):
    print "Match 3"








