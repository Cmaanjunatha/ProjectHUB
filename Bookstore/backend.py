import mysql.connector;


class Database:
    def __init__(self,):
        self.conn = mysql.connector.connect(database='db', user='root', password='root', host='localhost')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE Persons (Personid int NOT NULL AUTO_INCREMENT,"
                         "LastName varchar(255) NOT NULL,FirstName varchar(255),Age int,PRIMARY KEY (Personid))")
        self.conn.commit()

    def insert(self,title, author, year, isbn):
        #the NULL parameter is for the auto-incremented id
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (title,author,year,isbn))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()

        return rows

    def search(self,title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? "
                    "OR isbn = ?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id = ?", (id,))
        self.conn.commit()
        #conn.close()

    def update(self,id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        self.conn.commit()

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()
