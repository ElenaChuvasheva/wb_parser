from pydantic import BaseModel


def snake_to_camel(snake_str: str) -> str:
    if snake_str == "":
        return snake_str

    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


class ItemBase(BaseModel):
    nm_id: int


class ItemInput(ItemBase):
    pass


class ColorSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ItemUpSert(ItemBase):
    name: str
    brand: str
    brand_id: int
    site_brand_id: int
    supplier_id: int
    sale: int
    price: int
    sale_price: int
    rating: int
    feedbacks: int

    class Config:
        orm_mode = True
        alias_generator = snake_to_camel
        allow_population_by_field_name = True


class ItemSchema(ItemUpSert):
    colors: list[ColorSchema]

    class Config:
        orm_mode = True
        alias_generator = snake_to_camel
        allow_population_by_field_name = True
