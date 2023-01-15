from sqlalchemy import Column, Integer, String, Float

from database import Base


class Ativo(Base):
    __tablename__ = 'Ativos'

    id = Column(Integer, primary_key=True, index=True)
    valor = Column(Float, index=True)
    papel = Column(String, index=True)
    tipo = Column(String, index=True)
