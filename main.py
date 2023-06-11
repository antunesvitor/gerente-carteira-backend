from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    dbs = SessionLocal()
    try:
        yield dbs
    finally:
        dbs.close()

# Add uma posicao
@app.post("/ativo", response_model=schemas.Ativo)
def create_ativo(ativo: schemas.AtivoCreate, dbs: Session = Depends(get_db)):
    db_ativo = crud.get_ativo_by_name(dbs, ativo.papel)

    if db_ativo:
        raise HTTPException(status_code=400, detail='Ativo já adicionado')

    return crud.create_ativo(db_session=dbs, ativo=ativo)

@app.get('/ativo', response_model=list[schemas.Ativo])
def read_ativos(skip: int = 0, limit: int = 100, dbs: Session = Depends(get_db)):
    ativos = crud.get_ativos(dbs, skip=skip, limit=limit)
    return ativos

@app.post("/posicao", response_model=schemas.Posicao)
def create_posicao(posicao: schemas.PosicaoCreate, dbs: Session = Depends(get_db)):
    db_posicao = crud.get_posicao_by_name(dbs, posicao.nome)

    if db_posicao:
        raise HTTPException(status_code=400, detail='Posicão já adicionada')

    return crud.create_posicao(db_session=dbs, posicao=posicao)


@app.get('/posicao', response_model=list[schemas.Posicao])
def read_posicao(skip: int = 0, limit: int = 100, dbs: Session = Depends(get_db)):
    ativos = crud.get_posicoes(dbs, skip=skip, limit=limit)
    return ativos
