from typing import List  
from pydantic import BaseModel
from decimal import Decimal

class MarcaBase(BaseModel):
    nome: str
class MarcaCreate(MarcaBase):
    pass
class Marca(MarcaBase):
    id: int
    class Config:
        orm_mode = True
class PaginatedMarca(BaseModel):
    limit: int
    offset: int
    data: List[Marca]

class ModeloBase(BaseModel):
    nome: str
    id_marca: int
class ModeloCreate(ModeloBase):
    pass
class Modelo(ModeloBase):
    id: int
    class Config:
        orm_mode = True
class PaginatedModelo(BaseModel):
    limit: int
    offset: int
    data: List[Modelo]

class ModeloBase(BaseModel):
    nome: str
    id_marca: int
class ModeloCreate(ModeloBase):
    pass
class Modelo(ModeloBase):
    id: int
    marca: Marca = {}
    class Config:
        orm_mode = True
class PaginatedModelo(BaseModel):
    limit: int
    offset: int
    data: List[Modelo]

class CarroBase(BaseModel):
    nome: str
    id_modelo: int
    renavam: int
    placa: str
    valor: Decimal
    ano: int  
class CarroCreate(CarroBase):
    pass
class Carro(CarroBase):
    id: int
    modelo: Modelo = {}
    class Config:
        orm_mode = True
class PaginatedCarro(BaseModel):
    limit: int
    offset: int
    data: List[Carro]