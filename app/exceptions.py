from functools import partial

from fastapi import HTTPException, status

ItemNotFoundDBException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='Item not found in database')


# BadRequestDBException = partial(
#    HTTPException, status_code=status.HTTP_400_BAD_REQUEST)


ItemNotFoundShopException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='Item not found in wildberries')
