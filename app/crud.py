from sqlalchemy.orm import Session

from app import models, schemas


def create_item(db: Session, item: schemas.ItemSchema):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_item(db: Session, nm_id: int):
    return db.query(
        models.Item).filter(models.Item.nm_id == nm_id).first()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def delete_item(db: Session, nm_id: int):
    item_number = db.query(models.Item).filter(
        models.Item.nm_id == nm_id).delete()
    db.commit()
    return item_number
