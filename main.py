import psycopg2
import datetime
import os
import export1

rota = export1


# Conexão com db
conn = psycopg2.connect("dbname=northwind user=postgres password=admin")
print("Connection established")
cur = conn.cursor()




rota.export_table.usar("categories")
rota.export_table.usar("customer_customer_demo")
rota.export_table.usar("customer_demographics")
rota.export_table.usar("customers")
rota.export_table.usar("employee_territories")
rota.export_table.usar("employees")
rota.export_table.usar("orders")
rota.export_table.usar("products")
rota.export_table.usar("region")
rota.export_table.usar("shippers")
rota.export_table.usar("suppliers")
rota.export_table.usar("territories")
rota.export_table.usar("us_states")
rota.export_table.usar("order_details")






conn.commit()
cur.close()
conn.close()