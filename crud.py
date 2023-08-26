from sqlalchemy.orm import Session

import models, schemas

# ATIVO METHODS ========================================================================================================
def get_ativo(db_session: Session, ativo_id: int):
    return db_session.query(models.Ativo).filter(models.Ativo.id == ativo_id).first()

def get_ativo_by_name(db_session: Session, ativo_papel: str):
    return db_session.query(models.Ativo).filter(models.Ativo.papel == ativo_papel).first()

def get_ativos(db_session: Session, skip: int = 0, limit: int = 100):
    return db_session.query(models.Ativo).offset(skip).limit(limit).all()

def create_ativo(db_session: Session, ativo: schemas.AtivoCreate):
    db_ativo = models.Ativo(valor=ativo.valor, papel=ativo.papel, tipo=ativo.tipo)
    db_session.add(db_ativo)
    db_session.commit()
    db_session.refresh(db_ativo)
    return db_ativo

# ======================================================================================================================

# POSICAO METHODS ======================================================================================================
def get_posicao(db_session: Session, posicao_id:int):
    return db_session.query(models.Posicao).filter(models.Posicao.id == posicao_id).first()

def get_posicoes(db_session: Session, skip: int = 0, limit: int = 100):
    return db_session.query(models.Posicao).offset(skip).limit(limit).all()

def get_posicao_by_name(db_session: Session, posicao_nome: str):
    return db_session.query(models.Posicao).filter(models.Posicao.nome == posicao_nome).first()

def create_posicao(db_session: Session, posicao: schemas.PosicaoCreate):
    db_posicao = models.Posicao(nome=posicao.nome, quantidade=posicao.quantidade,
                            valor=posicao.valor, precoMedio=posicao.precoMedio,
                            valorInvestido=posicao.valorInvestido, posicaoAtual=posicao.posicaoAtual,
                            lucroPrejuizo=posicao.lucroPrejuizo)

    db_session.add(db_posicao)
    db_session.commit()
    db_session.refresh(db_posicao)
    return db_posicao

# ======================================================================================================================

# EMPRESA METHODS ======================================================================================================

def create_empresa(db_session: Session, empresa: schemas.EmpresaCreate):
    db_empresa = models.Empresa(nome= empresa.nome, cnpj=empresa.cnpj)

    db_session.add(db_empresa)
    db_session.commit(db_empresa)
    db_session.refresh(db_empresa)
    return db_empresa

def get_empresa(db_session: Session, id: int):
    return db_session.query(models.Empresa).filter(models.Empresa.id == id).first()

def get_empresa_by_cnpj(db_session: Session, cnpj: str):
    return db_session.query(models.Empresa).filter(models.Empresa.cnpj == cnpj).first()
