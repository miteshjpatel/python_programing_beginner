from dbm.dumb import _Database
import psycopg2


#connect to the db
con = psycopg2.connect(
            host = "mjUbuntu",
            database = "atadb",
            user = "ata",
            password = "SapGss123"
)

#cursor
cur = con.cursor()

cur.execute("insert into test (name, address) values(%s, %s)", ("Yogita", "900 West st, ST Louis, MI"))
con.commit()  

#execute query
cur.execute("select name, address from test")

rows = cur.fetchall()
for r in rows:
    print(f"name: {r[0]} address: {r[1]}")
    
  
cur.close()

#close the connection
con.close()