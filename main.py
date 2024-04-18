from fastapi import FastAPI
from src.routes import health_router, count_vowels_router

app = FastAPI()

app.include_router(health_router)
app.include_router(count_vowels_router)
