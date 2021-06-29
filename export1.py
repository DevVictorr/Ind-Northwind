import psycopg2
from datetime import datetime
import os
import pandas as pd
import sqlite3
import sqliteShow


mostrar = sqliteShow



now = datetime.now() 
date_time = now.strftime("-%m-%d-%Y --- %H;%M;%S")
str(date_time)


# Conexão com db
conn = psycopg2.connect("dbname=northwind user=postgres password=admin")
print("Connection established")
curr = conn.cursor()



class export_table():
    

    def usar(tabela_name):
         

         pasta = 'C:/data/postgres/%s' %(tabela_name)
         if os.path.isdir(pasta): # verificar se diretorio ja existe
            now = datetime.now() 
            date_time = now.strftime("-%m-%d-%Y --- %H;%M;%S")
            str(date_time)
            os.mkdir("C:/data/postgres/%s/%s%s" %(tabela_name,tabela_name,date_time))
            local1 = ("C:/data/postgres/%s/%s%s" %(tabela_name,tabela_name,date_time))
            sql3 = "COPY %s TO '%s/%s.csv' CSV HEADER;"%(tabela_name,local1,tabela_name)
            sql2 = "COPY %s TO '%s/%s.db' CSV HEADER;"%(tabela_name,local1,tabela_name)
            curr.execute(sql2)
            curr.execute(sql3)
         else:
            os.mkdir(pasta) # aqui vai criar a pasta se nao existir
            print ('Pasta criada com sucesso!')
            now = datetime.now() 
            date_time = now.strftime("-%m-%d-%Y --- %H;%M;%S")
            str(date_time)
            os.mkdir("C:/data/postgres/%s/%s%s" %(tabela_name,tabela_name,date_time))
            local1 = ("C:/data/postgres/%s/%s%s" %(tabela_name,tabela_name,date_time))
            sql3 = "COPY %s TO '%s/%s.csv' CSV HEADER;"%(tabela_name,local1,tabela_name)
            sql2 = "COPY %s TO '%s/%s.db' CSV HEADER;"%(tabela_name,local1,tabela_name)
            curr.execute(sql2)
            curr.execute(sql3)


    def orders(tabela_name):

          pasta = 'C:/data/postgres/%s' %(tabela_name)
          if os.path.isdir(pasta): # verificar se diretorio ja existe
            now = datetime.now() 
            date_time = now.strftime("-%m-%d-%Y --- %H;%M;%S")
            str(date_time)
            os.mkdir("C:/data/postgres/%s/%s%s" %(tabela_name,tabela_name,date_time))
            local1 = ("C:/data/postgres/%s/%s%s" %(tabela_name,tabela_name,date_time))
            sql3 = "COPY %s TO '%s/%s.csv' CSV HEADER;"%(tabela_name,local1,tabela_name)
            sql2 = "COPY %s TO '%s/%s.db' CSV HEADER;"%(tabela_name,local1,tabela_name)
            curr.execute(sql2)
            curr.execute(sql3)

            # conecta no sqlite
            conn = sqlite3.connect('%s.db'%(tabela_name))
            # carrega a data do csv
            stud_data = pd.read_csv('%s/%s.csv'%(local1,tabela_name))
            # escreve  a data no sql
            stud_data.to_sql(tabela_name, conn, if_exists='replace', index=False)
            # Cria um "cursor"
            cur = conn.cursor()
            # Grava e mostra resultado
            for row in cur.execute('SELECT * FROM %s'%(tabela_name)):
             print(row)

          else:
            os.mkdir(pasta) # aqui vai criar a pasta caso nao exista
            print ('Pasta criada com sucesso!')
            now = datetime.now() 
            date_time = now.strftime("-%m-%d-%Y --- %H;%M;%S")
            str(date_time)
            os.mkdir("C:/data/postgres/%s/%s%s" %(tabela_name,tabela_name,date_time))
            local1 = ("C:/data/postgres/%s/%s%s" %(tabela_name,tabela_name,date_time))
            sql3 = "COPY %s TO '%s/%s.csv' CSV HEADER;"%(tabela_name,local1,tabela_name)
            sql2 = "COPY %s TO '%s/%s.db' CSV HEADER;"%(tabela_name,local1,tabela_name)
            curr.execute(sql2)
            curr.execute(sql3)

            # conecta no sqlite
            conn = sqlite3.connect('%s.db'%(tabela_name))
            # carrega a data do csv
            stud_data = pd.read_csv('%s/%s.csv'%(local1,tabela_name))
            # escreve  a data no sql
            stud_data.to_sql(tabela_name, conn, if_exists='replace', index=False)
            # Cria um "cursor"
            cur = conn.cursor()
            # Grava e mostra resultado
            for row in cur.execute('SELECT * FROM %s'%(tabela_name)):
             print(row)



def back():

    export_table.usar("categories")
    export_table.usar("customer_customer_demo")
    export_table.usar("customer_demographics")
    export_table.usar("customers")
    export_table.usar("employee_territories")
    export_table.usar("employees")
    export_table.usar("products")
    export_table.usar("region")
    export_table.usar("shippers")
    export_table.usar("suppliers")
    export_table.usar("territories")
    export_table.usar("us_states")
    export_table.orders("orders")
    export_table.orders("order_details")
    
    mostrar.mostrar1()
    mostrar.mostrar2()