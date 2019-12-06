import psycopg2

try:
    connection = psycopg2.connect(user="postgres", password="admin", host="127.0.0.1", port=5432, database="postgres" )

    cursor = connection.cursor()
    cursor.execute('SELECT version();')


    record = cursor.fetchone()
    print("fecth record", record)

except(Exception, psycopg2.Error) as error:
    print("exception", error)


finally:
    if(connection):
        cursor.close()
        connection.close()
        print("database connection get closed")
