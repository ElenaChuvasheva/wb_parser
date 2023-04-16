import requests

from app import exceptions, schemas


def get_from_wb(nm_id: int):
    session = requests.Session()
    res = session.get(f'https://card.wb.ru/cards/detail?nm={nm_id};')
    try:
        item_dict = res.json().get('data').get('products').pop()
    except IndexError:
        raise exceptions.ItemNotFoundShopException
    colors_schemas_list = [schemas.ColorSchema(**color) for color in item_dict['colors']]
    item_dict['price'] = item_dict.pop('priceU')
    item_dict['salePrice'] = item_dict.pop('salePriceU')
    item_schema = schemas.ItemUpSert(nm_id=nm_id, **item_dict)
    return (colors_schemas_list, item_schema,)
