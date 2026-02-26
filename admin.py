from fastapi import APIRouter
from shutdown import turn_off, turn_on

router = APIRouter()

@router.post("/admin/off")
def off():
    turn_off()
    return {"AI":"OFF"}

@router.post("/admin/on")
def on():
    turn_on()
    return {"AI":"ON"}
