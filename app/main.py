from fastapi import FastAPI
from app.routers import books

app = FastAPI(title="Book Library API")

app.include_router(books.router, prefix="/books", tags=["books"])
