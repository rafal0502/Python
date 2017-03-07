#Statyczne metody sa podobne do metody klas, z wyjatkiem, ze nie przyjmuja
#zadnych dodatkowych argumentow, sa identyczne jak funkcje tylko ze naleza do
#klas. Oznacza sie je przez uzycie staticmethod decorator'a


class Pizza:
    def __init__(self,toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese","onions","spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)

#static method behave like plain functions,except for the fact that you
#can call them from an instance of the class
