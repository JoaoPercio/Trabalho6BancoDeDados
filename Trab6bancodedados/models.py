from sqlalchemy import Column, Integer, String, SmallInteger, Date, ForeignKey, Table, Numeric
from sqlalchemy.orm import relationship
from database import Base

class Marca(Base):
    __tablename__ = 'marca'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50))
    modelos = relationship("Modelo", back_populates="marca")

class Modelo(Base):
    __tablename__ = 'modelo'
    
    id = Column(Integer, primary_key=True, index=True)
    id_marca = Column(Integer, ForeignKey("marca.id"), nullable=False)
    nome = Column(String(50))
    marca = relationship("Marca", back_populates="modelos")
    carros= relationship("Carro", back_populates="modelo")

class Carro(Base):
    __tablename__ = 'carro'

    id = Column(Integer, primary_key=True, index=True)
    id_modelo = Column(Integer, ForeignKey("modelo.id"), nullable=False)
    nome = Column(String(50))
    renavam = Column(Integer)
    placa = Column(String(7))
    valor = Column(Numeric(10,2))
    ano = Column(Integer)
    modelo = relationship("Modelo", back_populates="carros")
    