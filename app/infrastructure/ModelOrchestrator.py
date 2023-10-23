from .ModelProvider import ModelProvider
from pydantic import BaseModel, HttpUrl


class ImageResult(BaseModel):
    url: HttpUrl
    name: str

class ModelOrchestrator:
    def __init__(self):
        self.model = ModelProvider().get_model()

    def orchestrate_response(self, prompt: str) -> ImageResult:
        return ImageResult(url=self.model.generate(prompt), name='test image')
