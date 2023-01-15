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
