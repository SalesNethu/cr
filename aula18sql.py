import mysql.connector

def mexer_no_banco(query):
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute(query)
    conexao.commit()
    cursor.close()
    conexao.close()
    return "alteeração realizada com sucesso"


def consultar_banco(query):
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute(query)
    lista = cursor.fetchall()
    cursor.close()
    conexao.close()
    return lista





db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Mysql102030",
    "database": "locadora"
}

conexao = mysql.connector.connect(**db_config)
cursor = conexao.cursor()
cursor.execute("select*from filmes")
lista_de_filmes = cursor.fetchall()
cursor.close()
conexao.close()


print(lista_de_filmes)

#conexao = mysql.connector.connect(**db_config)
#cursor = conexao.cursor()
#titulo_filme = str(input("digite o titulo do filme: "))
#genero_filme = str(input("digite o genero do filme: "))
#ano_filme = str(input("digite o ano de lançamento: "))
#cursor.execute(f"""INSERT INTO 
#filmes 
#(titulo, genero, ano_lancamento) 
#VALUES 
#('{titulo_filme}', '{genero_filme}', {ano_filme})""")
#conexao.commit()
#cursor.close()
#conexao.close()






todos_os_files = consultar_banco("select*from filmes")
filmes_pos_2005 = consultar_banco("select titulo from filmes where ano_lancamento > 2005")




titulo_filme = str(input("digite o titulo do filme: "))
genero_filme = str(input("digite o genero do filme: "))
ano_filme = str(input("digite o ano de lançamento: "))

query = (f"""
INSERT INTO filmes
(titulo, genero, ano_lancamento)
VALUES
('{titulo_filme}', '{genero_filme}', {ano_filme})
""")

print(mexer_no_banco(query))