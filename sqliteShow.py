import pandas as pd
import sqlite3



def mostrar1():
    #Conecta ao DB, se nao existir ele cria o arquivo.
    with sqlite3.connect("order_details.db") as con:
        #Seleciona tudo * dentro da tabela order_details
         sql = "SELECT * FROM order_details"
         #Coloca tudo oque coletou na variavel SQL e jogou para DF coom pandas.
         df = pd.read_sql_query(sql, con)
         #Mostra os primeiros e ultimos resultados no console.
         print (df.head)

def mostrar2():
    with sqlite3.connect("orders.db") as con:
         sql = "SELECT * FROM orders"
         df = pd.read_sql_query(sql, con)
         print (df.head)
