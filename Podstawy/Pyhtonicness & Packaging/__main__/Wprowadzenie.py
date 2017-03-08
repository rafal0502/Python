# Wiekszosc programow w Pythonie to moduly ktore importujemy
#lub skrypty, ktore cos robia

#Czasami uzyteczne jest by stworzyc plik ktory robi obydwie te rzeczy
#By to zrobic trzeba umiescic kod skryptu wewnatrz
#if __name__ == __main__
#to sprawia,ze plik nie wykona sie gdy zostanie zaimportowany

def function():
    print ('This is a module function')

if __name__ == "__main__":
    print ('This is a script')

# Python interpreter running module (the source file)
# as the main program , it sets the special __name__
# variable to have a value __main__
# if this file is being imported from another module
# __name__ will be set to the module's name

"""
x = 1
y = x
if __name__ == "__main__":
    z=3
do 'z' nie bedzie mozna sie dostac jesli ten kod zostanie
zaimportowany jako modul

Ten caly plik mozemy zaimportowac jako modul do innego-
dalsza czesc w "Importowanie.py"
"""

