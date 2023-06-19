from sqlalchemy.orm import Session
import models, schemas

#Marca

#SELECT * FROM marca;
def get_all_marcas(db: Session, offset: int, limit: int):
    return db.query(models.Marca).offset(offset).limit(limit).all()

#SELECT * FROM marca WHERE id = <id>;
def get_marca_by_id(db: Session, marca_id: int):
    db_marca = db.query(models.Marca).get(marca_id)
    return db_marca

#INSERT INTO marca VALUES ('mercedes',);
def create_marca(db: Session, marca: schemas.MarcaCreate):
    db_marca = models.Marca(**marca.dict())
    db.add(db_marca)
    db.commit()
    db.refresh(db_marca)
    return db_marca

#UPDATE marca SET nome = 'marca editada' WHERE id = <id>;
def update_marca(db: Session, marca_id: int, marca: schemas.MarcaCreate):
    db_marca = get_marca_by_id(db, marca_id)
    db_marca.nome = marca.nome
    db.commit()
    db.refresh(db_marca)
    return db_marca

#DELETE FROM marca WHERE id = <id>;
def delete_marca_by_id(db: Session, marca_id: int):
    db_marca = get_marca_by_id(db, marca_id)
    db.delete(db_marca)
    db.commit()
    return

#modelo

#SELECT * FROM modelo;
def get_all_modelos(db: Session, offset: int, limit: int):
    return db.query(models.Modelo).offset(offset).limit(limit).all()

#SELECT * FROM modelo WHERE id = <id>;
def get_modelo_by_id(db: Session, modelo_id: int):
    db_modelo = db.query(models.Modelo).get(modelo_id)
    return db_modelo

#INSERT INTO modelo VALUES ('modelo1', 1);
def create_modelo(db: Session, modelo: schemas.ModeloCreate):
    get_marca_by_id(db, modelo.id_marca)
    db_modelo = models.Modelo(id_marca=modelo.id_marca, nome=modelo.nome)
    db.add(db_modelo)
    db.commit()
    db.refresh(db_modelo)
    return db_modelo

#UPDATE modelo SET nome = 'modelo editado' WHERE id = <id>;
def update_modelo(db: Session, modelo_id: int, modelo: schemas.ModeloCreate):
    db_modelo = get_modelo_by_id(db, modelo_id)
    db_modelo.nome = modelo.nome
    db.commit()
    db.refresh(db_modelo)
    return db_modelo

#DELETE FROM modelo WHERE id = <id>;
def delete_carro_by_id(db: Session, modelo_id: int):
    db_modelo = get_modelo_by_id(db, modelo_id)
    db.delete(db_modelo)
    db.commit()
    return

#carro

#SELECT * FROM carro;
def get_all_carros(db: Session, offset: int, limit: int):
    return db.query(models.Carro).offset(offset).limit(limit).all()

#SELECT * FROM carro WHERE id = <id>;
def get_carro_by_id(db: Session, carro_id: int):
    db_carro = db.query(models.Carro).get(carro_id)
    return db_carro

#INSERT INTO carro VALUES ('carro4', 1);
def create_carro(db: Session, carro: schemas.CarroCreate):
    get_modelo_by_id(db, carro.id_modelo)
    db_carro = models.Carro(id_modelo=carro.id_modelo, nome=carro.nome, renavam=carro.renavam, placa=carro.placa, valor=carro.valor, ano=carro.ano)
    db.add(db_carro)
    db.commit()
    db.refresh(db_carro)
    return db_carro

#UPDATE carro SET nome = 'carro editado' WHERE id = <id>;
def update_carro(db: Session, carro_id: int, carro: schemas.CarroCreate):
    db_carro = get_modelo_by_id(db, carro_id)
    db_carro.nome = carro.nome
    db_carro.renavam = carro.renavam
    db_carro.placa = carro.placa
    db_carro.valor = carro.valor
    db_carro.ano = carro.ano
    db.commit()
    db.refresh(db_carro)
    return db_carro

#DELETE FROM carro WHERE id = <id>;
def delete_carro_by_id(db: Session, carro_id: int):
    db_carro = get_carro_by_id(db, carro_id)
    db.delete(db_carro)
    db.commit()
    return