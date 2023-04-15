from functools import partial

from fastapi import HTTPException, status

ItemNotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='Item not found')

BadRequestException = partial(
    HTTPException, status_code=status.HTTP_400_BAD_REQUEST)
