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

@app.post("/ativo", response_model=schemas.Ativo)
def create_ativo(ativo: schemas.AtivoCreate, dbs: Session = Depends(get_db)):
    db_ativo = crud.get_ativo_by_name(dbs, ativo.papel)

    if db_ativo:
        raise HTTPException(status_code=400, detail='Ativo já adicionado')

    return crud.create_ativo(db_session=dbs, ativo=ativo)


@app.get('/ativos', response_model=list[schemas.Ativo])
def read_ativos(skip: int = 0, limit: int = 100, dbs: Session = Depends(get_db)):
    ativos = crud.get_ativos(dbs, skip=skip, limit=limit)
    return ativos
