#@Properties provides a way of customizing access to instance attribiutes
#Ogolnie uzywamy ich jak chcemy ustawic settery i gettery

class Pizza:
    def __init__(self,toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
#pizza.pineapple_allowed = True bedzie blad can't set attribute


print("==========Inny przyklad==========")


class Person:
    def __init__(self,age):
        self.age = int(age)

    @property
    def isAdult(self):
        if self.age > 18:
            return True
        else:
            return False

Rafal = Person(22)
print(Rafal.isAdult)


#gettery i settery
#The getter gets the value. To define setter, we use decorator of the same
#name as the property,followed by a dot and the setter keyword.

class Pizza:
    def __init__(self,toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed


    @pineapple_allowed.setter
    def pineapple_allowed(self,value):
        if value:
            password = input("Enter the password:")
        if password == "Sw0rdf1sh!":
            self._pineapple_allowed = value
        else:
            raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese","tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)


















