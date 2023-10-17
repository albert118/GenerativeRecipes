from fastapi import FastAPI

from .routers import images, test

app = FastAPI()

app.include_router(images.router)
app.include_router(test.router)
