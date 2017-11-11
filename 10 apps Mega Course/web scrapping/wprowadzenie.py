import requests
from bs4 import BeautifulSoup

r = requests.get("http://pythonhow.com/example.html")   # pobranie zawartości strony
c = r.content

# print(c)  # wyświetlenie całej zawartości strony


soup = BeautifulSoup(c,"html.parser")
# print(soup.prettify())  # wyrzucenie uporządkowanego html takiego jak na stronie


all=soup.find_all("div",{"class":"cities"})  # soup.find_all("div",{"class":"cities"})[0] pierwszy element obiektu Tag, który obsługuje ineksowanie
# Londyn= all[0].find_all("h2")[0].text    # to zero, żeby pozbyć się listy a potem bierzemy sam tekst czyli London


for item in all:
    print(item.find_all("h2")[0].text)


# Dla paragrafów
for item in all:
    print(item.find_all("p")[0].text)
