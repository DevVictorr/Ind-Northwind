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


def categories():

    pasta = 'C:/data/postgres/categories'
    if os.path.isdir(pasta): # vemos de este diretorio ja existe
            os.mkdir("C:/data/postgres/categories/categories%s" %(date_time))
            local1 = ("C:/data/postgres/categories/categories%s" %(date_time))
            sql2 = "COPY orders TO '%s/categories.csv' CSV HEADER;"%(local1)
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print(cur.execute(sql2))
    else:
        os.mkdir(pasta) # aqui criamos a pasta caso nao exista
        print ('Pasta criada com sucesso!')

        os.mkdir("C:/data/postgres/categories/categories%s" %(date_time))
        local1 = ("C:/data/postgres/categories/categories%s" %(date_time))
        sql2 = "COPY orders TO '%s/categories.csv' CSV HEADER;"%(local1)
        print(cur.execute(sql2))

    #


def customer_customer_demo():

    pasta = 'C:/data/postgres/customer_customer_demo'
    if os.path.isdir(pasta): # vemos de este diretorio ja existe
            os.mkdir("C:/data/postgres/customer_customer_demo/customer_customer_demo%s" %(date_time))
            local1 = ("C:/data/postgres/customer_customer_demo/customer_customer_demo%s" %(date_time))
            sql2 = "COPY orders TO '%s/customer_customer_demo.csv' CSV HEADER;"%(local1)
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print(cur.execute(sql2))
    else:
        os.mkdir(pasta) # aqui criamos a pasta caso nao exista
        print ('Pasta criada com sucesso!')

        os.mkdir("C:/data/postgres/customer_customer_demo/customer_customer_demo%s" %(date_time))
        local1 = ("C:/data/postgres/customer_customer_demo/customer_customer_demo%s" %(date_time))
        sql2 = "COPY orders TO '%s/customer_customer_demo.csv' CSV HEADER;"%(local1)
        print(cur.execute(sql2))

        
def customer_demographics():

    pasta = 'C:/data/postgres/customer_demographics'
    if os.path.isdir(pasta): # vemos de este diretorio ja existe
            os.mkdir("C:/data/postgres/customer_demographics/customer_demographics%s" %(date_time))
            local1 = ("C:/data/postgres/customer_demographics/customer_demographics%s" %(date_time))
            sql2 = "COPY orders TO '%s/customer_demographics.csv' CSV HEADER;"%(local1)
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print(cur.execute(sql2))
    else:
        os.mkdir(pasta) # aqui criamos a pasta caso nao exista
        print ('Pasta criada com sucesso!')

        os.mkdir("C:/data/postgres/customer_demographics/customer_demographics%s" %(date_time))
        local1 = ("C:/data/postgres/customer_demographics/customer_demographics%s" %(date_time))
        sql2 = "COPY orders TO '%s/customer_demographics.csv' CSV HEADER;"%(local1)
        print(cur.execute(sql2))


def customers():

    pasta = 'C:/data/postgres/customers'
    if os.path.isdir(pasta): # vemos de este diretorio ja existe
            os.mkdir("C:/data/postgres/customers/customers%s" %(date_time))
            local1 = ("C:/data/postgres/customers/customers%s" %(date_time))
            sql2 = "COPY orders TO '%s/customers.csv' CSV HEADER;"%(local1)
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print(cur.execute(sql2))
    else:
        os.mkdir(pasta) # aqui criamos a pasta caso nao exista
        print ('Pasta criada com sucesso!')

        os.mkdir("C:/data/postgres/customers/customers%s" %(date_time))
        local1 = ("C:/data/postgres/customers/customers%s" %(date_time))
        sql2 = "COPY orders TO '%s/customers.csv' CSV HEADER;"%(local1)
        print(cur.execute(sql2))



def employee_territories():

    pasta = 'C:/data/postgres/employee_territories'
    if os.path.isdir(pasta): # vemos de este diretorio ja existe
            os.mkdir("C:/data/postgres/employee_territories/employee_territories%s" %(date_time))
            local1 = ("C:/data/postgres/employee_territories/employee_territories%s" %(date_time))
            sql2 = "COPY orders TO '%s/employee_territories.csv' CSV HEADER;"%(local1)
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print(cur.execute(sql2))
    else:
        os.mkdir(pasta) # aqui criamos a pasta caso nao exista
        print ('Pasta criada com sucesso!')

        os.mkdir("C:/data/postgres/employee_territories/employee_territories%s" %(date_time))
        local1 = ("C:/data/postgres/employee_territories/employee_territories%s" %(date_time))
        sql2 = "COPY orders TO '%s/employee_territories.csv' CSV HEADER;"%(local1)
        print(cur.execute(sql2))



def employees():

    pasta = 'C:/data/postgres/employees'
    if os.path.isdir(pasta): # vemos de este diretorio ja existe
            os.mkdir("C:/data/postgres/employees/employees%s" %(date_time))
            local1 = ("C:/data/postgres/employees/employees%s" %(date_time))
            sql2 = "COPY orders TO '%s/employees.csv' CSV HEADER;"%(local1)
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print(cur.execute(sql2))
    else:
        os.mkdir(pasta) # aqui criamos a pasta caso nao exista
        print ('Pasta criada com sucesso!')

        os.mkdir("C:/data/postgres/employees/employees%s" %(date_time))
        local1 = ("C:/data/postgres/employees/employees%s" %(date_time))
        sql2 = "COPY orders TO '%s/employees.csv' CSV HEADER;"%(local1)
        print(cur.execute(sql2))
    

