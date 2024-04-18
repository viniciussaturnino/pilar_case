from fastapi import APIRouter, status

from ..schemas import SortRequest
from ..services import SortWordsService

router = APIRouter(
    prefix='/sort-words',
    tags=['sort-words']
)


@router.post('/', status_code=status.HTTP_200_OK)
def post(request: SortRequest):
    service = SortWordsService(words=request.words)
    return service.sort_words(order=request.order)
