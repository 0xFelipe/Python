from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///banco.db', echo=True)
Base = declarative_base()

class Filme(Base):
    __tablename__ = 'filmes'
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)

Base.metadata.create_all(engine)

# Inserindo dados no banco de dados

def adicionar_filme(titulo, ano, nota):
    Session = sessionmaker(bind=engine)
    session = Session()
    novo_filme = Filme(titulo=titulo, ano=ano, nota=nota)
    session.add(novo_filme)
    session.commit()
    session.close()

# adicionar_filme('Os Vingadores', 2012, 8.0)
# adicionar_filme('Os Vingadores: A Era de Ultron', 2015, 7.3)

# Atualizando dados no banco de dados

def atualizar_filme(id, titulo=None, ano=None, nota=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter(Filme.id == id).first()
    if filme:
        if titulo is not None:
            filme.titulo = titulo
        if ano is not None:
            filme.ano = ano
        if nota is not None:
            filme.nota = nota
        session.commit()
    session.close()

# atualizar_filme(1, titulo='Os Vingadores: Ultimato', ano=2019, nota=8.4)

# Excluindo dados do banco de dados

def excluir_filme(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter(Filme.id == id).first()
    if filme:
        session.delete(filme)
        session.commit()
    session.close()

# excluir_filme(1)