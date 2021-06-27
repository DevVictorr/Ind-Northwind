import psycopg2
from datetime import datetime
import os

now = datetime.now() 
date_time = now.strftime("-%m-%d-%Y --- %H;%M;%S")
str(date_time)


# Conexão com db
conn = psycopg2.connect("dbname=northwind user=postgres password=admin")
print("Connection established")
cur = conn.cursor()



class export_table():
    

    def usar(tabela_name):
         

         pasta = 'C:/data/postgres/%s' %(tabela_name)
         if os.path.isdir(pasta): # vemos de este diretorio ja existe
            os.mkdir("C:/data/postgres/%s/%s%s" %(tabela_name,tabela_name,date_time))
            local1 = ("C:/data/postgres/%s/%s%s" %(tabela_name,tabela_name,date_time))
            sql2 = "COPY orders TO '%s/%s.csv' CSV HEADER;"%(local1,tabela_name)
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print(cur.execute(sql2))
         else:
            os.mkdir(pasta) # aqui criamos a pasta caso nao exista
            print ('Pasta criada com sucesso!')

            os.mkdir("C:/data/postgres/%s/%s%s" %(tabela_name,tabela_name,date_time))
            local1 = ("C:/data/postgres/%s/%s%s" %(tabela_name,tabela_name,date_time))
            sql2 = "COPY orders TO '%s/%s.csv' CSV HEADER;"%(local1,tabela_name)
            print(cur.execute(sql2))


            