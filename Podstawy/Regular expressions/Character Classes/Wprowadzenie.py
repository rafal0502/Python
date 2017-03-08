#Character classes provide a way to match only one of a
#specific set of character

import re

pattern = r"[ae]"

if re.search(pattern,"grey"):
    print "Match"

if re.search(pattern,"qwartyuiop"):
    print "Match 2"

if re.search(pattern,"rhythm myths"):
    print "Match 3"

    