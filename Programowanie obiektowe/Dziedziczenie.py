
class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color

#Klasa nadrzedna to Superclass'a
#Klasa dziedziczaca po innej jest nazywana Subclass'a

    def jedz(self):
        print('Mniam, mniam')

class Cat(Animal):
    def mrr(self):
        print("Mrr...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

    def jedz(self):
        print("Mmm, kosc")
        super().jedz()
        

fido = Dog("Fido" , "brown")
print(fido.color)
fido.bark()
print("============")
fido.jedz()
#Nadpisywanie;
print("============")
mruczek = Cat("mruczek","czarno-bialy")
mruczek.jedz()


#Dziedzicznie 'w kolko' jest nie mozliwe




