import re

pattern = r"a(bc)(de)(f(g)h)i"




match = re.match(pattern,"abcdefghijklmnop")
if match:
    print match.group() #to samo co group(0) zwraca wszystko
    print match.group(0)
    print match.group(1)
    print match.group(2)    #zwraca drugi od lewej
    print match.groups()
    