# ? oznacza zero albo jedno powtorzenie


import re

pattern = r"ice(-)?cream"

if re.match(pattern,"ice-cream"):
    print 'Match 1'

if re.match(pattern,"icecream"):
    print 'Match 2'

if re.match(pattern,"sausages"):
    print 'Match 3'


if re.match(pattern,"ice-ice"):
    print 'Match 4'

#matching both 'color' and 'colour'
#pattern=r"colo(u)?r


#nawiasy klamrowe {x,y} powtorzenia miedzy x i y {0,1} <=> ?

pattern2 = r"9{1,3}$"  #matches string that have 1 to 3 nines

if re.match(pattern2,"9"):
    print 'Dziewiatka'

if re.match(pattern2,"999"):
    print '3 dziewiatki'

if re.match(pattern2, "99999"):
    print 'piec dziewiatek'

    






