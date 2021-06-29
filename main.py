import export1
import time

rota = export1


while True:
   
   #Chamar funcao de exportar Tabelas para DB/CSV
   rota.back()
   
   #Tempo que vai exportar novamente (criar novas pastar e arquivos)
   time.sleep(3) #86400 segundos = 24 horas // a cada 24 horas vai  fazer novos backup
   

conn.commit()
cur.close()
conn.close()




    