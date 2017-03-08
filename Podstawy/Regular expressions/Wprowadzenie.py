#Wyrazenia regularne sa stosowane np. po to, by sprawdzac poprawnosc wprowadzanych danych
#Mozna uzyskac do nich dostep uzywajac re module, ktory jest czescia wyrazenia regularnego
#w regularnych wyrazeniach mozna uzywac skladni re"expression" (tzw. raw stringi)

#raw string don't escape anything , which makes use of regular expressions easier





#Funkcion that match patterns are re.search and re.findall
#re.search finds a match of a pattern anywhere in the string

#re.findall returns a list of all substrings that match a pattern


import re

pattern=r"spam"

if re.match(pattern,"eggsspamsausagespam"):
    print("Match")
else:
    print("No match")


if re.search(pattern,"eggsspamsausagespam"):
    print('Match')
else:
    print('No match')


print(re.findall(pattern,"eggsspamsausagespam"))

print '======================================='

pattern_2 = r'pam'

match = re.search(pattern_2, "eggspamsausagesuate")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

print '========================================'


napis = 'My name is David. Hi David.'

pattern =r"David"
nowy_napis = re.sub(pattern,"Amy",napis)
print(nowy_napis)






















