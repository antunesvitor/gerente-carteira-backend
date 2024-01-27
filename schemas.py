import datetime
from pydantic import BaseModel

class AtivoBase(BaseModel):
    valor: float
    papel: str
    id_tipo: int
    id_empresa: int

class AtivoCreate(AtivoBase):
    pass

class Ativo(AtivoBase):
    id: int

    class Config:
        orm_mode = True


class PosicaoBase(BaseModel):
    id_usuario: int
    id_ativo: int
    quantidade: int

class PosicaoCreate(PosicaoBase):
    pass

class Posicao(PosicaoBase):
    id: int

    class Config:
        orm_mode = True


class EmpresaBase(BaseModel):
    nome: str
    cnpj: str

class EmpresaCreate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    id: int

    class Config:
        orm_mode = True


class TipoAtivoBase(BaseModel):
    tipo: str

class TipoAtivoCreate(TipoAtivoBase):
    pass

class TipoAtivo(TipoAtivoBase):
    id: int

    class Config:
        orm_mode = True


class CompraBase(BaseModel):
    id_usuario: int
    id_ativo: int
    preco_unitario: float
    quantidade: int

class CompraCreate(CompraBase):
    pass

class Compra(CompraBase):
    id: int
    data_compra: datetime.datetime
    
    class Config:
        orm_mode = True

class UsuarioBase(BaseModel):
    name: str
    password: str

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int

    class Config:
        orm_mode = True