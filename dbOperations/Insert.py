import mysql.connector;

conn = mysql.connector.connect(database='mydb', user='root', password='root', host='localhost')

if conn.is_connected():
    print("Connected to mydb")

    cursor = conn.cursor()
    try:
        cursor.execute("insert into emp values(6,'chandranna',30000)")
        conn.commit()
        print("employee added")
    except:
        conn.rollback()

    cursor.close()
    conn.close()