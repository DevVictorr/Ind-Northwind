# Ind-Northwind

Permite que você faça backup de tabelas de um DB como em nosso exemplo vai ser usado Northwind no Postgresql a cada "X" tempo por exemplo: a cada hora, dia, segundos etc...

Criando novas pastas com datas exatas no  formato (Mes-Dia-Ano - Hr;Mn;Sg), Criando em especial 2 Tabelas especificas na pasta Raiz do projeto em .db para fazer conexão com sqlite3.
Permitindo visualizar e trabalhar com os dados para futuras analises (orders e order_details)

nota: [Prints](https://github.com/DevVictorr/Ind-Northwind#prints)

# Requisitos
[Postgresql](https://www.postgresql.org/)

[northwind.sql](https://github.com/DevVictorr/Ind-Northwind/tree/master/arquivos_necessarios)

[orderdetails.csv](https://github.com/DevVictorr/Ind-Northwind/tree/master/arquivos_necessarios)

# Instalação
Baixe este repositório
Abra um prompt de comando dentro da pasta
Baixe as Bibliotecas, modulos, Pacotes por exemplo, "pip install psycopg2"

Postgresql- (Adicione ao DB [northwind.sql](https://github.com/DevVictorr/Ind-Northwind/tree/master/arquivos_necessarios) e [orderdetails.csv](https://github.com/DevVictorr/Ind-Northwind/tree/master/arquivos_necessarios) ao seu Postgresql)

Crie um diretorio **C:\data\postgres**


# Configuração
Primeiro temos que se atentar ao erro mais comum que é a configuração da conexão ao  banco de dados, no arquivo **(export1.py)**

**dbname =**    para colocar o nome da sua DB
**user =**     para colocar seu user, no meu caso é postgres
**password =** para colocar sua senha para acessar o   db, no meu caso ficaria como abaixo:

-conn = psycopg2.connect("**dbname**=northwind **user**=postgres **password**=admin")

Ainda no arquivo **(export1.py)** veremos a segunte **func: def back():**
Podemos alterar os nomes das tabelas que serão feitas a export/backup/conexão alterando no final do comando por exemplo:
No caso abaixo o "categories" é o nome de uma tabela que vai ser feita a ação, no seu caso pode ser outro. 

export_table.usar("**categories**")

 Caso não queira usar a linha mas quer deixar guardado você pode comentar ela e colocar um # antes, por exemplo:
 
 #export_table.usar("**categories**")
 
 Uma parte muito importante é sobre os .db que vão ser conectado a outro banco de dados depois, oonde você deve colocar entre as aspas "o nome de sua tabela",
 são eles:
 
 export_table.orders("**orders**")
 
 export_table.orders("**order_details**")
 
 
Temos o arquivo **(main.py)** temos a seguinte linha:

 time.sleep(86400) Esse numero grande é quantos segundos tem um dia para que ele possa refazer o backup a cada 24 horas. Você pode alterar
 para seu uso, de 10 em 10 segundos ou 3600 (Uma hora), Em um update proximo irei colocar para fazer entre X a Y.
 
Agora temos um arquivo chamado (**sqliteShow.py**):

A configuração dele é simples, é os .db que foi falado logo la acima que vão ser criados na pasta raiz e enviados para o sqlite3 são eles (orders e order_details).

A alteração é praticamente igual as outras, mudando o que esta entre as aspas "order_details.db" para ser o nome de seu DB escolhido nas linhas:
 export_table.orders("**orders**")
 export_table.orders("**order_details**")

Ficaria assim no arquivo (**sqliteShow.py**):
def mostrar1():
with sqlite3.connect("**order_details.db**") as con:
sql = "SELECT * FROM **order_details**"
No def mostrar2() segue a mesma logica.

# Iniciar

Execute main.py

Os dados dos .db criados podem ser visto no console com pandas PD.head, ou com o  [sqlitebrowser](https://sqlitebrowser.org/)


# Print's

# Antes
![Antes](https://i.imgur.com/ayRvWXu.png)

# Depois
![Depois](https://i.imgur.com/zCQD8Xd.png)

# Pasta criada com horario e data
![Pasta criada com horario e data](https://i.imgur.com/43JaJiK.png)

# Arquivos criados
![Arquivos criados](https://i.imgur.com/r4VeouD.png)

# Verificar com Pandas
![Verificar com Pandas](https://i.imgur.com/biPez7Q.png)

# Verificar com sqlitebrowser
![Verificar com Pandas](https://i.imgur.com/TME1kH9.png)







 
 
 
 
 
 
 
 
 
 
