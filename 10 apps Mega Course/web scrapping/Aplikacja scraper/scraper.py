# -*- coding: utf-8 -*-
import requests
import pandas
from bs4 import BeautifulSoup


r=requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c=r.content

soup=BeautifulSoup(c,"html.parser")
# print(soup.prettify().encode("utf-8"))  # trzeba było  zakodować w utf-8 inaczej błąd


all=soup.find_all("div",{"class":"propertyRow"})
#print(all)

# mamy liste i w każdym jej elemencie wyszukujemy podelement
# all[0].find_all("h4",{"class":"propPrice"})


all[0].find("h4",{"class":"propPrice"})     # możemy dać find bo mamy tylko jedną price na każy element
# print((all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ",""))) # tylko jeden element tutaj wypisaliśmy



l = []
for item in all:
    d = {}  # tworzymy słownik, żeby dodać do niego elementy a potem w data frame wylądują
    d["Address"]=item.find_all("span",{"class","propAddressCollapse"})[0].text
    d["Locality"]=item.find_all("span",{"class","propAddressCollapse"})[1].text
    d["Price"]=item.find("h4",{"class","propPrice"}).text.replace("\n","").replace(" ","")
    try:
        d["Beds"]=item.find("span",{"class","infoBed"}).find("b").text
    except:
        d["Beds"]=None
    try:
        d["Area"]=item.find("span",{"class","infoSqFt"}).find("b").text
    except:
        d["Area"]=None
    try:
        d["Full Baths"]=item.find("span",{"class","infoValueFullBath"}).find("b").text
    except:
        d["Full Baths"]=None
    try:
        d["Half Baths"]=item.find("span",{"class","infoValueHalfBath"}).find("b").text
    except:
        d["Half Baths"]=None
    for column_group in item.find_all("div",{"class":"columnGroup"}):
        for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
            if "Lot Size" in feature_group.text:
                d["Lot Size"]=feature_name.text
    l.append(d)

df = pandas.DataFrame(l)
print(df)

df.to_csv("Output.csv")
