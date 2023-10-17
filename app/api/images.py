from ..infrastructure.ModelProvider import ModelProvider
from fastapi import APIRouter

router = APIRouter(
    prefix="/images",
    responses={404: {"description": "Not found"}},
)


@router.post('/')
def generate_image(prompt: str):
    '''Get a new image'''
    model_provider = ModelProvider()
    return model_provider.do_thing()
