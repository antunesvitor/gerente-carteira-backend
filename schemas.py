from pydantic import BaseModel

class AtivoBase(BaseModel):
    valor: float
    papel: str
    tipo: str

class AtivoCreate(AtivoBase):
    pass

class Ativo(AtivoBase):
    id: int

    class Config:
        orm_mode = True

class PosicaoBase(BaseModel):
    nome: str
    quantidade: float
    valor: float
    precoMedio: float
    valorInvestido: float
    posicaoAtual: float
    lucroPrejuizo: float

class PosicaoCreate(PosicaoBase):
    pass

class Posicao(PosicaoBase):
    id: int

    class Config:
        orm_mode = True
