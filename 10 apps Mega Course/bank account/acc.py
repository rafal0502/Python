class Account:

    def __init__(self,filepath):
        self.filepath=filepath          # filepath z __init__ jest to ta sama co filepath i ona idzie do self.filepath żebyśmy ją mogli użyć w commit (bo wewnątrz klasy możemy używać)
        with open(filepath, 'r') as file:
            self.balance=int(file.read())


    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount


    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))



class Checking(Account):                        # dziedziczenie
    """This class generate checking account objects"""

    type = "checking"                           # class variable - współdzielona przez wszystkie obiekty danej klasy

    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee = fee                          # żeby można było użyć self.fee w metodzie amount (w zasadzife fee)

    def transfer(self,amount):
       self.balance=self.balance - amount - self.fee

jacks_checking = Checking("jack.txt",1)
jacks_checking.transfer(100)
print(jacks_checking.balance)
jacks_checking.commit()
print(jacks_checking.type)

john_checking = Checking("john.txt",1)
john_checking.transfer(100)
print(john_checking.balance)
john_checking.commit()
print(john_checking.type)

print(john_checking.__doc__)
