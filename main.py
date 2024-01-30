from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
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

# ==================================================================================================
@app.post("/posicao", response_model=schemas.Posicao)
def create_posicao(posicao: schemas.PosicaoCreate, dbs: Session = Depends(get_db)):
    db_posicao_user = crud.get_posicao_by_user_and_ativo(dbs, posicao.id_usuario, posicao.id_ativo)

    if db_posicao_user:
        raise HTTPException(status_code=400, detail='Posição já cadastrada')

    return crud.create_posicao(db_session=dbs, posicao=posicao)

@app.put("/posicao", response_model=schemas.Posicao)
def update_posicao(posicao: schemas.Posicao, dbs: Session = Depends(get_db)):
    return crud.update_posicao(db_session=dbs, posicao=posicao)

@app.get('/posicao', response_model=list[schemas.Posicao])
def read_posicao(skip: int = 0, limit: int = 100, dbs: Session = Depends(get_db)):
    ativos = crud.get_posicoes(dbs, skip=skip, limit=limit)
    return ativos

# ==================================================================================================

@app.post('/empresa', response_model=schemas.Empresa)
def create_empresa(empresa: schemas.EmpresaCreate, dbs: Session = Depends(get_db)):
    db_empresa = crud.get_empresa_by_cnpj(db_session=dbs, cnpj=empresa.cnpj)

    if db_empresa:
        raise HTTPException(status_code=400, detail='empresa já adicionada')

    return crud.create_empresa(db_session=dbs, empresa=empresa)

@app.get('/compra', response_model=list[schemas.Compra])
def read_compra(id_usuario:int, dbs: Session = Depends(get_db)):
    compras = crud.get_compras_by_user(dbs, id_user=id_usuario)
    return compras

@app.post('/compra', response_model=schemas.Compra)
def create_compra(compra: schemas.CompraCreate, dbs: Session = Depends(get_db)):
    return crud.create_compra(db_session=dbs, compra=compra)

# Usuario ===========================================================================
@app.get('/usuario', response_model=schemas.Usuario)
def read_user(id: int, dbs: Session = Depends(get_db)):
    return crud.get_user(db_session=dbs, id=id)

@app.post('/usuario', response_model=schemas.Usuario)
def create_usuario(usuario: schemas.UsuarioCreate, dbs: Session = Depends(get_db)):
    db_usuario = crud.get_user_by_name(db_session=dbs, user_name=usuario.name)

    if db_usuario:
        raise HTTPException(status_code=400, detail='Usuário já adicionado')

    return crud.create_usuario(db_session=dbs, usuario=usuario)
