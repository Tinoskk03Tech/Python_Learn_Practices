# fichier: main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Modèle de données
class Item(BaseModel):
    id: int
    name: str
    price: float

# Base de données simulée
db: List[Item] = []

# Création de l'application FastAPI
app = FastAPI(title="Microservice Exemple", version="1.0")

@app.get("/items", response_model=List[Item])
def get_items():
    return db

@app.post("/items", response_model=Item)
def create_item(item: Item):
    # Vérifier si l'ID existe déjà
    if any(existing.id == item.id for existing in db):
        raise HTTPException(status_code=400, detail="ID déjà existant")
    db.append(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item non trouvé")

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur mon microservice FastAPI"}