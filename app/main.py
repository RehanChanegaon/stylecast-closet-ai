from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="StyleCast Closet AI",
    description="Backend system for outfit building and recommendation logic",
    version="1.0.0"
)

app.include_router(router)