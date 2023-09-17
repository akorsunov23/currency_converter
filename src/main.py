import uvicorn
from fastapi import FastAPI

app = FastAPI(title='Currency Converter')


if __name__ == "__main__":
	uvicorn.run(app="src.main:app", log_level="INFO", reload=True)
