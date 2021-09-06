from fastapi import FastAPI
from routes.index import url

app = FastAPI()

app.include_router(url)
