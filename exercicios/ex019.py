import sqlalchemy

from sqlalchemy import create_engine, Column, Integer, Text, Date, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

conexao = "mysql+mysqlconnector://apostila:AssassinsCreed2017@localhost/LojaDeGames"

engine = create_engine(conexao, echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)

from sqlalchemy import Column, Integer, Text, Date, String, Sequence

class Jogo(Base):
   __tablename__ = 'Jogos'
   id = Column(Integer, Sequence('jogo_id_seq'), primary_key=True)
   nome = Column(String(255))
   plataforma = Column(String(50))
   data_lancamento = Column(Date())
   descricao = Column(Text(255))

# Criar um novo jogo
nome = "Assassin's Creed"
plataforma = "XBOX 360"
data_lancamento = datetime("2017","11","13")
descricao = ""
novo = Jogo(nome,plataforma,data_lancamento,descricao)

# Iniciar uma sessão
session = Session()

# Adicionar e confirmar o novo jogo
session.add(novo)
session.commit()

# Recuperar todos os Jogos
jogos = session.query(Jogo).all()

for jogo in jogos:
   print(jogo.id, jogo.nome, jogo.descricao)

# Atualizar a descricão de um jogo
jogo = session.query(Jogo).filter(id=1).first()
jogo.descricao = "Assassin's Creed foi o primeiro jogo da franquia ..."

# Confirmar Atualização
session.commit()

# Excluir um jogo
jogo = session.query(Jogo).filter_by(id=1).first()
session.delete(jogo)

# Confirmar Exclusão
session.commit()
session.close()