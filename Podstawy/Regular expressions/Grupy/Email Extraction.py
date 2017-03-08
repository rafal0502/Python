import re

#creating program to extract email adresses from a string


str = "Please contact info@sololearn.com for assistance"

#our goal is to extract the substring info@sololearn.com


pattern = r"([\w\.-\]+)@([w\.-]+)(\.[\w\.]+)" #kropka poprzedzona
#ukosnikiem zeby traktowac ja jak character


#[\w\.-]+ matches one or more word character, dot or dash


match = re.search(pattern, str)
if match:
    print match.group()


