#zapisywanie do pliku nowy_plik.txt tekstu 

file = open("nowy_plik.txt","w")
file.write("Ala ma kota")
file.close()


file = open("nowy_plik.txt", "r")
print(file.read())
file.close()
