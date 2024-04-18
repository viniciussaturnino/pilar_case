from fastapi import APIRouter, status

router = APIRouter(
    prefix='/health_check',
    tags=['health_check']
)


@router.get('/', status_code=status.HTTP_200_OK)
def index():
    return {"message": "Hello, World!"}
