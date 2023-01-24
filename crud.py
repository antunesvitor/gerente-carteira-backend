from sqlalchemy.orm import Session

import models, schemas

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