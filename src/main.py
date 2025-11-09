from fastapi import FastAPI
from src.external_api import router as external_router

app = FastAPI(title="Lab 7–9 External API + Docker + Cloud")
app.include_router(external_router.router)
