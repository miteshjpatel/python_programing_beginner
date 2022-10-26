import errno
import psycopg2
import getpass

dbuser = input("Enter db User id: ")
dbpass = getpass.getpass("Enter db password: ")
# connect to the db


try:
    conn = psycopg2.connect(
        host="mjUbuntu",
        database="atadb",
        user=dbuser,
        password=dbpass
    )

    # cursor
    cur = conn.cursor()

    # Insert data in table COMPANY
    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (1, 'Paul', 32, 'California', 20000.00 )")

    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

    # Commit to database
    conn.commit()

except Exception as error:
    print(error)
finally:
    if cur is not None:
        # Close cursor
        cur.close()
    if conn is not None:
        # Close connection to DB
        conn.close()
