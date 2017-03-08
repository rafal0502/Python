#Grupa moze byc przekazana jako argument jak meta znak * czy ?

import re

pattern = r"egg(spam)*"

if re.match(pattern,"egg"):
    print 'Match 1'

if re.match(pattern,"eggsspamspamspam"):
    print 'Match 2'

if re.match(pattern,"spam"):
    print 'Match 3'


