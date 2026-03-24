from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Incident Copilot")

app.include_router(router)