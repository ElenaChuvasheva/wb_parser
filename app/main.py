from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.post('/items/')
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_items(db, item)
