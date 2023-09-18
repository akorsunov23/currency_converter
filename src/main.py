import uvicorn
from fastapi import FastAPI

from src.converter.routers import converter_app

app = FastAPI(title="Currency Converter")

app.include_router(converter_app)

if __name__ == "__main__":
    uvicorn.run(app="src.main:app", log_level="info", reload=True)
