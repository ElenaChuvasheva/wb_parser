from sqlalchemy.orm import Session

from app import models, schemas


def upsert_item(db: Session, item: schemas.ItemUpSert,
                colors_schemas_list: list[schemas.ColorSchema]):
    db_item = models.Item(**item.dict())
    model_item = db.merge(db_item)

    old_color_ids = {color.id for color in model_item.colors}
    new_color_ids = {color.id for color in colors_schemas_list}
    if new_color_ids != old_color_ids:
        model_item.colors = []
        color_models = [models.Color(
            **color_schema.dict()) for color_schema in colors_schemas_list]
        db_colors = []
        for index, color in enumerate(color_models):
            color_models[index] = db.merge(color)
            db_colors.append(schemas.ColorSchema.from_orm(color))
        model_item.colors = color_models
    db_item = schemas.ItemSchema.from_orm(model_item)
    db.commit()
    return db_item


def get_item(db: Session, nm_id: int):
    return db.query(
        models.Item).filter(models.Item.nm_id == nm_id).first()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def delete_item(db: Session, nm_id: int):
    items_number = db.query(models.Item).filter(
        models.Item.nm_id == nm_id).delete()
    db.commit()
    return items_number
