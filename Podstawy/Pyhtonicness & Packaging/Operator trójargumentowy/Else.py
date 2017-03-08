for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")

for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2")

#else moze byc uzyte z while'em i for'em (jak zakonczymy petle
#nie normalnie (break'iem) to sie nie wykona instrukcja else


#code within it is only executed if no error occurs in the try
#statment

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)


