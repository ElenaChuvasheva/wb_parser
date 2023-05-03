from fastapi import Depends, FastAPI, Response, status
from sqlalchemy.orm import Session

from app import crud, exceptions, schemas, wildberries
from app.database import SessionLocal

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
def update_or_create_item(item_input: schemas.ItemInput,
                          db: Session = Depends(get_db)):
    wb_result = wildberries.get_from_wb(item_input.nm_id)
    colors_schemas_list = wb_result[0]
    item = wb_result[1]
    db_item = crud.upsert_item(db, item, colors_schemas_list)
    return db_item


@app.get('/items/{nm_id}/', response_model=schemas.ItemSchema)
def read_item(nm_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, nm_id)
    if db_item is None:
        raise exceptions.ItemNotFoundDBException
    return db_item


@app.get('/items/', response_model=list[schemas.ItemSchema])
def read_items(skip: int = 0, limit: int = 100,
               db: Session = Depends(get_db)):
    return crud.get_items(db, skip=skip, limit=limit)


@app.delete('/items/{nm_id}/')
def delete_item(nm_id: int, db: Session = Depends(get_db)):
    item_number = crud.delete_item(db, nm_id)
    if item_number == 0:
        raise exceptions.ItemNotFoundDBException
    return Response(status_code=status.HTTP_204_NO_CONTENT)
