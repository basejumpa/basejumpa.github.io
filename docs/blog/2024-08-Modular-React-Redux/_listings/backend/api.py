from fastapi import APIRouter
from backend.models import ValueResponse

router = APIRouter()

@router.get("/value", response_model=ValueResponse)
async def get_value():
    return ValueResponse(value=42)
