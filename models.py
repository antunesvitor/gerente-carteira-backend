from sqlalchemy import Column, Integer, String, Float

from database import Base


class Ativo(Base):
    __tablename__ = 'Ativos'

    id = Column(Integer, primary_key=True)
    valor = Column(Float)
    papel = Column(String)
    tipo = Column(String)


class Posicao(Base):
    __tablename__ = 'Posicoes'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    quantidade = Column(Float)
    valor = Column(Float)
    precoMedio = Column(Float)
    valorInvestido = Column(Float)
    posicaoAtual = Column(Float)
    lucroPrejuizo = Column(Float)
