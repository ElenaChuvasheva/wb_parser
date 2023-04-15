from pydantic import BaseModel


class ItemSchema(BaseModel):
    nm_id: int
    name: str
    brand: str | None
    brand_id: int | None
    site_brand_id: int | None
    supplier_id: int | None
    sale: int | None
    price: int | None
    sale_price: int | None
    rating: int | None
    feedbacks: int | None

    class Config:
        orm_mode = True
