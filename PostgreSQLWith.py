import errno
from unicodedata import name
import psycopg2
import psycopg2.extras
import getpass

dbuser = input("Enter db User id: ")
dbpass = getpass.getpass("Enter db password: ")
# connect to the db


try:
    with psycopg2.connect(
        host="mjUbuntu",
        database="atadb",
        user=dbuser,
        password=dbpass
    ) as conn:

        # cursor
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            # Update salary by 50%
            update_script = 'Update company SET salary = salary + (salary * 0.5)'
            cur.execute(update_script)

            # Delete script
            delete_script = 'delete from company where name = %s'
            delete_record = ('Mark',)
            cur.execute(delete_script, delete_record)

            cur.execute('SELECT * FROM COMPANY')
            for record in cur.fetchall():
                print(record['name'],  record['age'], record['address'])

            # Don't need commit with clause
            # conn.commit()

except Exception as error:
    print(error)
finally:
    # Don't need close cursor with clause
    # if cur is not None:
    #     # Close cursor
    #     cur.close()
    if conn is not None:
        # Close connection to DB
        conn.close()
