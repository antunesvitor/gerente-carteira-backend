from fastapi import Depends
import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import delete, insert
from sqlalchemy.sql import text
import crud
from models import TipoAtivo, Empresa, Ativo
import schemas
from database import engine


with Session(engine) as session:

    #limpar as tabelas
    print("removendo registros atuais")

    session.execute(delete(TipoAtivo))
    session.execute(delete(Empresa))
    session.execute(delete(Ativo))

    print("resetando index cache das tabelas")
    session.execute(text("ALTER SEQUENCE \"TiposAtivo_id_seq\" RESTART WITH 1"))
    session.execute(text("ALTER SEQUENCE \"Empresas_id_seq\" RESTART WITH 1"))
    session.execute(text("ALTER SEQUENCE \"Ativos_id_seq\" RESTART WITH 1"))

    print("cadastrando TipoAtivos")
    #Cadastrando tipoAtivo
    crud.create_tipo_ativo(db_session=session, tipo_ativo= schemas.TipoAtivoCreate(tipo="Ação"))
    crud.create_tipo_ativo(
        db_session=session,
        tipo_ativo= schemas.TipoAtivoCreate(tipo="Fundo de Investimentos Imobiliário"))
    crud.create_tipo_ativo(
        db_session=session,
        tipo_ativo= schemas.TipoAtivoCreate(tipo="Exchange-Traded Fund"))

    print('feito')

    data_empresas = pd.read_csv('data/convertcsv.csv')

    # print(data_empresas[0])

    lista_empresas = []
    lista_ativos = []
    for index, registro in data_empresas.iterrows():
        # print(registro["Empresa"])
        empresaObj = schemas.EmpresaCreate(nome=registro['Empresa'], cnpj=registro['CNPJ'])
        for ativo in registro['Código(s)'].splitlines():
            ativoObj = schemas.AtivoCreate(valor=0, papel=ativo, id_tipo=1, id_empresa=index + 1)
            lista_ativos.append(ativoObj)
        lista_empresas.append(empresaObj)

    print('inserindo empresas')
    result = session.scalars(insert(Empresa).returning(Empresa), lista_empresas)
    print('feito.')

    print('inserindo ativos')
    result = session.scalars(insert(Ativo).returning(Ativo), lista_ativos)
    print('feito.')

    session.commit()

    print(result)
