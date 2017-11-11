# postgresql

import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port=5432'")   # połączenie z bazą
    cur = conn.cursor()                 # obiekt kursor (coś ja wskaźnik)
     # tworzenie tabeli (bo baza danych to tabele)
    cur.execute("CREATE TABLE  IF NOT EXISTS store (item TEXT, quantity INTEGER,price REAL)")
    conn.commit()                       # zatwierdzenie zapytania do bazy
    conn.close()


def insert(item,quantity,price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port=5432'")
    cur = conn.cursor()
    # dobra praktyka, żeby utrudnić sql injection
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()



def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port=5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()     # wydobujemy dane i zapisujemy w rows
    conn.close()            # tylko wybieramy dane więc nie musimy commitować
    return rows



def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port=5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,)) # gdy mamy jeden parametr trzeba
                                                          # dać przecinek
    conn.commit()
    conn.close()


def update(quantity,price,item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port=5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price =%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()


create_table()
# insert("Apple",10,15)
# insert("Orange",10,15)
# delete("Orange")
update(20,15.0,"Apple")
print(view())
# update(11,6,"Water Glass")
# print(view())
