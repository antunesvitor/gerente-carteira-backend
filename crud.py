from sqlalchemy.orm import Session

import models
import schemas

# ATIVO METHODS =================================================================================
def get_ativo(db_session: Session, ativo_id: int):
    return db_session.query(models.Ativo).filter(models.Ativo.id == ativo_id).first()

def get_ativo_by_name(db_session: Session, ativo_papel: str):
    return db_session.query(models.Ativo).filter(models.Ativo.papel == ativo_papel).first()

def get_ativos(db_session: Session, skip: int = 0, limit: int = 100):
    return db_session.query(models.Ativo).offset(skip).limit(limit).all()

def create_ativo(db_session: Session, ativo: schemas.AtivoCreate):
    db_ativo = models.Ativo(valor=ativo.valor, papel=ativo.papel,
                            id_tipo=ativo.id_tipo, id_empresa=ativo.id_empresa)
    db_session.add(db_ativo)
    db_session.commit()
    db_session.refresh(db_ativo)
    return db_ativo

# =================================================================================================

# POSICAO METHODS =================================================================================
def get_posicao(db_session: Session, posicao_id:int):
    return db_session.query(models.Posicao).filter(models.Posicao.id == posicao_id).first()

def get_posicoes(db_session: Session, skip: int = 0, limit: int = 100):
    return db_session.query(models.Posicao).offset(skip).limit(limit).all()

def get_posicao_by_user(db_session: Session, user_id: int):
    return db_session.query(models.Posicao).filter(models.Posicao.id_usuario == user_id).first()

def create_posicao(db_session: Session, posicao: schemas.PosicaoCreate):
    db_posicao = models.Posicao(id_usuario=posicao.id_usuario, id_ativo=posicao.id_ativo,
                                quantidade=posicao.quantidade)

    db_session.add(db_posicao)
    db_session.commit()
    db_session.refresh(db_posicao)
    return db_posicao

#=============================================================================================

# EMPRESA METHODS ============================================================================

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

#==================================================================================================

def create_tipo_ativo(db_session: Session, tipo_ativo: schemas.TipoAtivoCreate):
    db_tipo_ativo = models.TipoAtivo(tipo=tipo_ativo.tipo)

    db_session.add(db_tipo_ativo)
    db_session.commit()
    db_session.refresh(db_tipo_ativo)
    return db_tipo_ativo

# COMPRAS ========================================================================================

def get_compras_by_user(db_session: Session, id_user: int):
    return db_session.query(models.Compra).filter(models.Compra.id_usuario == id_user).all()

def create_compra(db_session: Session, compra: schemas.Compra):
    db_compra = models.Compra(id_usuario=compra.id_usuario, id_ativo=compra.id_ativo,
                                preco_unitario=compra.preco_unitario, quantidade=compra.quantidade)

    db_session.add(db_compra)
    db_session.commit()
    db_session.refresh(db_compra)
    return db_compra

# Usuario ========================================================================================
def get_user(db_session: Session, id: int):
    return db_session.query(models.Usuario).filter(models.Usuario.id == id).first()

def get_user_by_name(db_session: Session, user_name: str):
    return db_session.query(models.Usuario).filter(models.Usuario.name == user_name).first()

def create_usuario(db_session: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(name=usuario.name, password=usuario.password)

    db_session.add(db_usuario)
    db_session.commit()
    db_session.refresh(db_usuario)
    return db_usuario