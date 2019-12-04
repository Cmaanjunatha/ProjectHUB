#Create Database in MySQL

#Create database hunk;
#Below is the last step, i.e. using methods of MySQL Connector Python to connect MySQL database. Let see the example now.

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='mydb',
                                         user='root',
                                         password='root')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)

        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
#After connecting to MySQL Server, you should get below output.

#Connected to MySQL Server version  5.7.25-log
#You're connected to database:  ('mydb',)
#MySQL connection is closed