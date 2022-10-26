import psycopg2
import getpass

dbuser = input("Enter db User id: ")
dbpass = getpass.getpass("Enter db password: ")
#connect to the db

try:
    conn = psycopg2.connect(
                host = "mjUbuntu",
                database = "atadb",
                user = dbuser,
                password = dbpass
    )

    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS COMPANY
        (ID INT PRIMARY KEY     NOT NULL,
        NAME           TEXT    NOT NULL,
        AGE            INT     NOT NULL,
        ADDRESS        CHAR(50),
        SALARY         REAL);''')
    print("Table created successfully")
    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()