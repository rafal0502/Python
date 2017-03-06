# W Pythonie nie jest uzywane narzedzie takie jak oznaczenia: prywatne etc.
# sluzace do blokowania dostepu do danych z klas i funkcji

#Metody prywatne w Python'ie to takie, ktore 'zniechecaja' do korzystania z zewnetrzengo kodu?


#Jedna z konwecji 'prywatyzacji' klas jest uzycie pojedynczego podkreslnika, ktory sprawia
#ze wyrazenie from module_name import* nie pobierze z wszystkich danych tak podkreslonych
#Przyklad nizej

class Queue:
    def __init__ (self,contents):
        self._hiddenlist = list(contents)

    def push(self,value):
        self._hiddenlist.insert(0,value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1,2,3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)


#'BARDZO' prywatne metody i atrybuty maja podwojne podkreslenie na poczatku nazwy.
#To powoduje,ze nie moga byc wywolane z zewnatrz klasy


#Double underscore - ich nazwy na tyle znieksztalcone? co oznacza,ze nie mozna sie do
#nich dostac z zewnatrz klasy, dalej mozna uzyskac do nich dostep z zewnatrz,ale trzeba
#podac jeszcze nazwe klasy z ktorej pochodza for example:

class Spam:
    __egg = 7
    def print__egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
print(s.__egg)









