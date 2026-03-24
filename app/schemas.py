from pydantic import BaseModel

class IncidentRequest(BaseModel):
    log: str