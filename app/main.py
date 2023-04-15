from fastapi import Depends, FastAPI, Response, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import crud, exceptions, models, schemas
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


@app.post('/items/', response_model=schemas.ItemSchema)
def create_item(item: schemas.ItemSchema, db: Session = Depends(get_db)):
    try:
        db_item = crud.create_item(db, item)
        return db_item
    except IntegrityError as error:
        raise exceptions.BadRequestException(detail=str(error))


@app.get('/items/{nm_id}/', response_model=schemas.ItemSchema)
def read_item(nm_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, nm_id)
    if db_item is None:
        raise exceptions.ItemNotFoundException
    return db_item


@app.get('/items/', response_model=list[schemas.ItemSchema])
def read_items(skip: int = 0, limit: int = 100,
               db: Session = Depends(get_db)):
    return crud.get_items(db, skip=skip, limit=limit)


@app.delete('/items/{nm_id}/')
def delete_item(nm_id: int, db: Session = Depends(get_db)):
    item_number = crud.delete_item(db, nm_id)
    if item_number == 0:
        raise exceptions.ItemNotFoundException
    return Response(status_code=status.HTTP_204_NO_CONTENT)
