import os
import uvicorn

from settings import app

if __name__ == "__main__":
    port = os.getenv("PORT", 8000)
    host = os.getenv("HOST", "0.0.0.0")

    uvicorn.run(
        app=app,
        host=host,
        port=port
    )
