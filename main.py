import os
from fastapi import FastAPI
import uvicorn

from src.routes import count_vowels_router, health_router, sort_words_router

app = FastAPI()

app.include_router(health_router)
app.include_router(count_vowels_router)
app.include_router(sort_words_router)

if __name__ == "__main__":
    port = os.getenv("PORT", 8000)
    host = os.getenv("HOST", "0.0.0.0")

    uvicorn.run(
        app=app,
        host=host,
        port=port
    )
