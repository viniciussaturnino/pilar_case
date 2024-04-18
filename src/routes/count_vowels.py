from fastapi import APIRouter, status

from ..schemas import BaseRequest
from ..services import CountVowelsService

router = APIRouter(
    prefix='/count-vowels',
    tags=['count-vowels']
)


@router.post('/', status_code=status.HTTP_200_OK)
def post(request: BaseRequest):
    service = CountVowelsService(words=request.words)
    return service.count_vowels()
