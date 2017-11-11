import sqlite3

class Database:
    # do db wysłana jest nazwa bazy "books.db"
    def __init__(self,db):                     # konstruktor - do self wysyłany jest obiekt Database() - to taka konwencja, że piszemy self
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def insert(self,title,author,year,isbn):       # gdy wywołujemy metodę to jest wysyłany obiekt tej klasy do niej dlatego trzeba dodać wszędzie self
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))  # null nada nam id - python automatycznie doda
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows


    def search(self,title="",author="",year="",isbn=""): # defaultowo ustawione na pusto żeby nie było błedu przy wyszukiwaniu gdy nie wpiszemy wszystkich argumentów
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        self.rows = self.cur.fetchall()
        return rows


    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()



    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
        







# insert("The Sun","John Smith",1912, 129484312)
# delete(3)
# update(4,"The moon","John Smith",1912,129481293)
# print(view())
# print(search(author="John Smith"))
