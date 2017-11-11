import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")   # połączenie z bazą
    cur = conn.cursor()                 # obiekt kursor (coś ja wskaźnik)
     # tworzenie tabeli (bo baza danych to tabele)
    cur.execute("CREATE TABLE  IF NOT EXISTS store (item TEXT, quantity INTEGER,price REAL)")
    conn.commit()                       # zatwierdzenie zapytania do bazy
    conn.close()


def insert(item,quantity,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    # dobra praktyka, żeby utrudnić sql injection
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()



def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()     # wydobujemy dane i zapisujemy w rows
    conn.close()            # tylko wybieramy dane więc nie musimy commitować
    return rows



def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,)) # gdy mamy jeden parametr trzeba
                                                          # dać przecinek
    conn.commit()
    conn.close()


def update(quantity,price,item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price =? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()


update(11,6,"Water Glass")
print(view())
