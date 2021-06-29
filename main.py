import psycopg2
import datetime
import os
import export1
import time
import sqliteShow

rota = export1
mostrar = sqliteShow

# Conexão com db
conn = psycopg2.connect("dbname=northwind user=postgres password=admin")
print("Connection established")
cur = conn.cursor()



while True:
   
   
   rota.back()
   
   
   time.sleep(3) #
   

conn.commit()
cur.close()
conn.close()




    