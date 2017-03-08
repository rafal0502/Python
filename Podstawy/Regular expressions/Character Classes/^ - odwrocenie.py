# ^ na poczatku sprawia,ze odwracamy wyraz
# This causes it to match any character other than the ones included
# inne znaki jak $ i . nie maja znaczenia wewnatrz klas
# ^ nie maja znaczenia chyba,ze sa pierwsze w class'ie


import re

pattern = r"[^A-Z]" #takie,ktore w calosci nie skladaja sie z [A-Z](dzieki ^)

if re.search(pattern, "this is all quiet"):
    print 'Match 1'

if re.search(pattern, "AbCdEfG123"):
    print 'Match 2'


if re.search(pattern, 'THISISALLSHOUTING'):
    print 'Match 3'




