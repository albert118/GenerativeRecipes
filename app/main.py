from fastapi import FastAPI

from .api import images, test

app = FastAPI()

app.include_router(images.router)
app.include_router(test.router)
