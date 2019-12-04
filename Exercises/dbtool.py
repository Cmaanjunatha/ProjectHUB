import mysql.connector;

conn = mysql.connector.connect(database='mydb', user='root', password='root', host='localhost')

if conn.is_connected():
    print("Connected to mydb")
cursor = conn.cursor()


def delete(id):
    delete = "delete from emp where id = '%d'"
    args = (id)
    try:
        cursor.execute(delete % args)
        conn.commit()
        print('emplyee id deleted')
    except:
        conn.rollback()


def update(id):
    update = "UPDATE emp SET name='gur',Sal=56000 where id='%d'"
    args = (id)
    try:
        cursor.execute(update % args)
        conn.commit()
        print('updated employee id')
    except:
        conn.rollback()


def insert(id, name, Sal):
    insert = "INSERT INTO emp values('%d','%s','%g')"
    args = (id, name, Sal)
    try:
        cursor.execute(insert % args)
        conn.commit()
        print('inserted data')
    except:
        conn.rollback()


def read():
    read = "select * from emp"
    try:
        cursor.execute(read)
        rows = cursor.fetchall()
        print("Total Number of Records", cursor.rowcount)

        for row in rows:
            print(row)
        conn.commit()
        print('reading data')
    except:
        conn.rollback()

    finally:
        cursor.close()
        conn.close()


# empid = int(input('Enter Emp id : '))
# delete(empid)


# empid = int(input("enter emp id: "))
# update(empid)

read()

# empid = int(input("enter emp id: "))
# name = str(input("Enter name: "))
# Sal = int(input("Enter Salary: "))
# insert(empid, name, Sal)
