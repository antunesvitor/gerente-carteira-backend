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
