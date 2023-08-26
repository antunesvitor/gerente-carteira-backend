from typing import List
from sqlalchemy import ForeignKey, String, Float
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
class Base(DeclarativeBase):
    pass

class TipoAtivo(Base):
    __tablename__ = 'TiposAtivo'

    id: Mapped[int] = mapped_column(primary_key=True)
    tipo: Mapped[str] = mapped_column(String(100))

    ativos: Mapped[List["Ativo"]] = relationship(back_populates='tipo')

class Empresa(Base):
    __tablename__ = 'Empresas'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(200))
    cnpj: Mapped[str] = mapped_column(String(20))

    ativos: Mapped[List["Ativo"]] = relationship(back_populates='empresa')

class Ativo(Base):
    __tablename__ = 'Ativos'

    id: Mapped[int] = mapped_column(primary_key=True)
    valor: Mapped[float] = mapped_column()
    papel: Mapped[str] = mapped_column(String(30))
    id_tipo: Mapped[int] = mapped_column(ForeignKey("TiposAtivo.id"))
    id_empresa: Mapped[int] = mapped_column(ForeignKey('Empresas.id'))

    tipo: Mapped["TipoAtivo"] = relationship(back_populates="ativos")
    empresa: Mapped["Empresa"] = relationship(back_populates="ativos")

class Posicao(Base):
    __tablename__ = 'Posicoes'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String)
    quantidade: Mapped[int] = mapped_column()
    valor: Mapped[float] = mapped_column(Float)
    precoMedio: Mapped[float] = mapped_column(Float)
    valorInvestido: Mapped[float] = mapped_column(Float)
    posicaoAtual: Mapped[float] = mapped_column(Float)
    lucroPrejuizo: Mapped[float] = mapped_column(Float)

class Usuario(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)

class Compra(Base):
    __tablename__ = 'Compras'

    id: Mapped[int]  = mapped_column(primary_key=True)
    idAtivo: Mapped[int] = mapped_column()
