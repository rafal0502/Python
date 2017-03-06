#Metody dodaja do klasy rozne funkcjonalnosci. Wszystkie metody musza miec 'self' jako ich
#pierwszy parametr


class Dog:
    legs = 4    # Klasy moga miec argumenty
                # Mozna miec do nich dostep z instancji klasy lub z samej klasy (patrz nizej)

    def __init__(self, name, colors):
        self.name = name
        self.colors = colors

    def bark(self):
        print("Woof!")

fido = Dog("Fido","brown")
print(fido.name)
fido.bark()

print(fido.legs)
print(Dog.legs)


