import psycopg2
import datetime
import os
import write1

rota = write1


# Conexão com db
conn = psycopg2.connect("dbname=northwind user=postgres password=admin")
print("Connection established")
cur = conn.cursor()





rota.categories()
rota.customer_customer_demo()
rota.customer_demographics()
rota.customers()
rota.employee_territories()







conn.commit()
cur.close()
conn.close()