#Magiczne metody to takie, ktore maja 2 podreslenia na poczatku i koncu nazwy funkcji
#Tworza funkcjonalnosci, ktorych nie moga stworzyc normalne metody

#Mozna tworzyc dzieki nim operatory! np. __add__ dla +

class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector2D(self.x + other.x, self.y + other.y)


first = Vector2D(5,3)
second = Vector2D(4,8)

result = first + second
print(result.x)
print(result.y)

