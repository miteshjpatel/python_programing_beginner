import psycopg2
import getpass

dbuser = input("Enter db User id: ")
dbpass = getpass.getpass("Enter db password: ")
#connect to the db
con = psycopg2.connect(
            host = "mjUbuntu",
            database = "atadb",
            user = dbuser,
            password = dbpass
)

#cursor
cur = con.cursor()

# cur.execute("insert into test (name, address) values(%s, %s)", ("Yogita", "900 West st, ST Louis, MI"))
# con.commit()  

#execute query
cur.execute("select name, address from test")

rows = cur.fetchall()
for r in rows:
    print(f"name: {r[0]} address: {r[1]}")
    
  
cur.close()

#close the connection
con.close()