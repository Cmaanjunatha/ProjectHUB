import mysql.connector;

conn = mysql.connector.connect(database='mydb', user='root', password='root', host='localhost')

if conn.is_connected():
    print("Connected to mydb")

cursor = conn.cursor()
cursor.execute('select * from emp')

row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()

cursor.close()
conn.close()

