from fastapi import APIRouter

router = APIRouter(
    prefix="/test",
    responses={404: {"description": "Not found"}},
)

@router.get('/ping')
def read_root():
    return 'pong'