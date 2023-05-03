from fastapi import HTTPException, status

ItemNotFoundDBException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='Item not found in database')


ItemNotFoundShopException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='Item not found in wildberries')
