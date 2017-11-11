from tkinter import *

window = Tk() # create empty window

def km_to_miles():
    miles=float(e1_value.get())*1.6                    # to objekt string, dlatego metoda taka
    t1.insert(END,miles)




b1 = Button(window,text="Execute",command=km_to_miles) # command to funkcja
                                                       # po naciśnięciu

b1.grid(row=0,column=0)                                # wywołanie przycisku

e1_value = StringVar()                                 # pobranie objektu string
e1 = Entry(window,textvariable=e1_value)               # wpisywanie tekstu
e1.grid(row=0,column=1)

t1 = Text(window,height=1,width=20)
t1.grid(row=0,column=2)


window.mainloop() # coś w rodzaju pętli, żeby okno progamu się nie zamknęło
