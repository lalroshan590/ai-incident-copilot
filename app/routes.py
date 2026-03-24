from fastapi import APIRouter
from app.ai_engine import analyze_incident
from app.schemas import IncidentRequest

router = APIRouter()

@router.get("/")
def health():
    return {"status": "running"}

@router.post("/analyze")
def analyze(request: IncidentRequest):
    try:
        result = analyze_incident(request.log)
        return {"analysis": result}
    except Exception as e:
        return {"error": str(e)}