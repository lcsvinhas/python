import mysql.connector

# CONFIGURAÇÃO DA CONEXÃO
conexao = mysql.connector.connect(
    user = "apostila",
    password = "AssassinsCreed@",
    host = "127.0.0.1",
    database = "LojaDeGames"
)

cursor = conexao.cursor()

query = "CREATE TABLE Jogos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255) NOT NULL,"
query += " plataforma VARCHAR(50), data_lancamento DATE, descricao TEXT);"
cursor.execute(query)
conexao.commit()

import datetime

lancamento = datetime.datetime(2017,11,13)

# INSERIR UM NOVO JOGO
query = "INSERT INTO Jogos (nome, plataforma, data_lancamento, descricao)"
query += "VALUES (%s, %s)"
dados = ("Assassin's Creed", "XBOX 360", lancamento, "Assassin's Creed ...")
cursor.execute(query, dados)

# CERTIFICAR-SE DE FAZER COMMIT PARA SALVAR AS ALTERAÇÕES
conexao.commit()

# RECUPERAR TODOS OS JOGOS
query = "SELECT * FROM Jogos"

cursor.execute(query)
jogos = cursor.fetchall()

for jogo in jogos:
    print(jogo)

# ATUALIZAR A DESCRIÇÃO DE UM JOGO
query = "UPDATE Jogos SET descricao = %s WHERE id = %s"
dados = ("O primeiro game da franquia ...", 1)

cursor.execute(query, dados)
conexao.commit()

# EXCLUIR UM JOGO
query = "DELETE FROM Jogos WHERE id = %s"
jogo_id = (1,)

cursor.execute(query, jogo_id)
conexao.commit()

cursor.close()
conexao.close()