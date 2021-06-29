import pandas as pd
import sqlite3



def mostrar1():
    with sqlite3.connect("order_details.db") as con:
         sql = "SELECT * FROM order_details"
         df = pd.read_sql_query(sql, con)
         print (df.head)

def mostrar2():
    with sqlite3.connect("orders.db") as con:
         sql = "SELECT * FROM orders"
         df = pd.read_sql_query(sql, con)
         print (df.head)
