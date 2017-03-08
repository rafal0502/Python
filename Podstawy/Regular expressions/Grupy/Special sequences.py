import re

pattern = r"(.+) \1"

match = re.match(pattern,"word word")
if match:
    print "Match 1"


match = re.match(pattern,"?! ?!")
if match:
    print "Match 2"

match = re.match(pattern,"abc cde")
if match:
    print "Match 3"


# for example" (abc|xyz) \1 match
#abc or xyz followed by the same thing


# \d \s and \w match digit whitespace and word character
#in ASCII thee're equivalent to [0-9],[\t\n\r\f\v] and
# [a-zA-Z0-9//_]
# konwecja duzych liter \D wyznaczaja wszystko poza digitami

print '==================================='

pattern2 = r"(\D+\d)"

match = re.match(pattern2, "Hi 999")

if match:
    print 'Match 1'

match = re.match(pattern2, "1,23,456!")
if match:
    print 'Match 2'

match = re.match(pattern2, "!$")
if match:
    print 'Match 3'


print '==================================='

pattern3 = r"\b(cat)\b"

match =re.search(pattern3, "The cat sat!")
if match:
    print 'Match 1'

match = re.search(pattern3, "We s>cat<tered?")
if match:
    print 'Match 2'

match = re.search(pattern3, "We scattered")
if match:
    print 'Match 3'

