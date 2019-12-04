import mysql.connector;

conn= mysql.connector.connect(
database='mydb',
user='root',
password='root',
host='localhost'
)

if conn.is_connected():
	print('connected to mydb')

cursor  = conn.cursor()

def update(id):
    str = "UPDATE emp SET sal=65000 where id='%s'"
    args =(id)
    try:
        cursor.execute(str % args)
        conn.commit()
        print('updated salary')

    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()



empid = int(input('enter emp id: '))
update(empid)