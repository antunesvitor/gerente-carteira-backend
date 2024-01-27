import datetime
from typing import List
from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.sql import func
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
    id_tipo: Mapped[int] = mapped_column(ForeignKey('TiposAtivo.id'))
    id_empresa: Mapped[int] = mapped_column(ForeignKey('Empresas.id'))

    tipo: Mapped["TipoAtivo"] = relationship(back_populates='ativos')
    empresa: Mapped["Empresa"] = relationship(back_populates='ativos')
    compras: Mapped[List['Compra']] = relationship(back_populates='ativo')
    posicoes: Mapped['Posicao'] = relationship(back_populates='ativo')


class Posicao(Base):
    __tablename__ = 'Posicoes'

    id: Mapped[int] = mapped_column(primary_key=True)
    id_usuario: Mapped[int] = mapped_column(ForeignKey('Users.id'))
    id_ativo: Mapped[int] = mapped_column(ForeignKey('Ativos.id'))
    quantidade: Mapped[int] = mapped_column()

    ativo: Mapped['Ativo'] = relationship(back_populates='posicoes')
    usuario: Mapped['Usuario'] = relationship(back_populates='posicoes')


class Usuario(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)

    compras: Mapped[List['Compra']] = relationship(back_populates='usuario')
    posicoes: Mapped[List['Posicao']] = relationship(back_populates='usuario')


class Compra(Base):
    __tablename__ = 'Compras'

    id: Mapped[int] = mapped_column(primary_key=True)
    id_usuario: Mapped[int] = mapped_column(ForeignKey('Users.id'))
    id_ativo: Mapped[int] = mapped_column(ForeignKey('Ativos.id'))
    preco_unitario: Mapped[float] = mapped_column()
    quantidade: Mapped[int] = mapped_column()
    data_compra: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    usuario: Mapped['Usuario'] = relationship(back_populates='compras')
    ativo: Mapped['Ativo'] = relationship(back_populates='compras')
