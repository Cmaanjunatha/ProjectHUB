import mysql.connector;


def delete(id):
    conn = mysql.connector.connect(database='mydb', user='root', password='root', host='localhost')

    if conn.is_connected():
        print("Connected to mydb")
        cursor = conn.cursor()
        str = "delete from emp where id = '%d'"
        args = (id)
        try:
            cursor.execute(str % args)
            conn.commit()
            print("deleted emp id")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()



empid = int(input('Enter Emp id : '))
delete(empid)