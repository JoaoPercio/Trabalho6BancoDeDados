from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from database import get_db, engine
import crud, models, schemas

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# marca

#SELECT * FROM marca WHERE id = <id>;
@app.get("/api/marcas/{marca_id}", response_model=schemas.Marca)
def get_marca_by_id(marca_id: int, db: Session = Depends(get_db)):
        return crud.get_marca_by_id(db, marca_id)

#SELECT * FROM marca;
@app.get("/api/marcas",  response_model=schemas.PaginatedMarca)
def get_all_marcas(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_marcas = crud.get_all_marcas(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_marcas}
    return response

#INSERT INTO marca VALUES ('mercedes',);
@app.post("/api/marcas",  response_model=schemas.Marca)
def create_marca(marca: schemas.MarcaCreate, db: Session = Depends(get_db)):
        return crud.create_marca(db, marca)

#UPDATE marca SET nome = 'marca editada' WHERE id = <id>;
@app.put("/api/marcas/{marca_id}",  response_model=schemas.Marca)
def update_marca(marca_id: int, marca: schemas.MarcaCreate, db: Session = Depends(get_db)):
        return crud.update_marca(db, marca_id, marca)

#DELETE FROM marca WHERE id = <id>;
@app.delete("/api/marcas/{marca_id}", )
def delete_marca_by_id(marca_id: int, db: Session = Depends(get_db)):
     return crud.delete_marca_by_id(db, marca_id)

# modelo

#SELECT * FROM modelo WHERE id = <id>;
@app.get("/api/modelos/{modelo_id}", response_model=schemas.Modelo)
def get_modelo_by_id(modelo_id: int, db: Session = Depends(get_db)):
        return crud.get_modelo_by_id(db, modelo_id)

#SELECT * FROM modelo;
@app.get("/api/modelos", response_model=schemas.PaginatedModelo)
def get_all_modelos(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_modelos = crud.get_all_modelos(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_modelos}
    return response

#INSERT INTO modelo VALUES ('modelo1', 1);
@app.post("/api/modelos",response_model=schemas.Modelo)
def create_modelo(modelo: schemas.ModeloCreate, db: Session = Depends(get_db)):
        return crud.create_modelo(db, modelo)

#UPDATE modelo SET nome = 'modelo editado' WHERE id = <id>;
@app.put("/api/modelos/{modelo_id}", response_model=schemas.Modelo)
def update_modelo(modelo_id: int, modelo: schemas.ModeloCreate, db: Session = Depends(get_db)):
        return crud.update_modelo(db, modelo_id, modelo)


#DELETE FROM modelo WHERE id = <id>;
@app.delete("/api/modelos/{modelo_id}")
def delete_modelo_by_id(modelo_id: int, db: Session = Depends(get_db)):
        return crud.delete_modelo_by_id(db, modelo_id)

# carro

#SELECT * FROM carro WHERE id = <id>;
@app.get("/api/carros/{carro_id}", response_model=schemas.Carro)
def get_carro_by_id(carro_id: int, db: Session = Depends(get_db)):
        return crud.get_carro_by_id(db, carro_id)

#SELECT * FROM carro;
@app.get("/api/carros",response_model=schemas.PaginatedCarro)
def get_all_carros(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_carros = crud.get_all_carros(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_carros}
    return response

#INSERT INTO carro VALUES ('carro4', 1);
@app.post("/api/carros", response_model=schemas.Carro)
def create_carro(carro: schemas.CarroCreate, db: Session = Depends(get_db)):
        return crud.create_carro(db, carro)
    
#UPDATE carro SET nome = 'carro editado' WHERE id = <id>;
@app.put("/api/carros/{carro_id}",response_model=schemas.Carro)
def update_carro(carro_id: int, carro: schemas.CarroCreate, db: Session = Depends(get_db)):
        return crud.update_carro(db, carro_id, carro)

#DELETE FROM carro WHERE id = <id>;
@app.delete("/api/carros/{carro_id}")
def delete_carro_by_id(carro_id: int, db: Session = Depends(get_db)):
        return crud.delete_carro_by_id(db, carro_id)
