from fastapi import APIRouter, Request
from device_lock import generate_fingerprint

router = APIRouter()

db = {}

@router.post("/login")
async def login(request: Request):
    data = await request.json()
    email = data["email"]
    password = data["password"]
    device = data["device"]

    fp = generate_fingerprint(device)

    if email not in db:
        db[email] = fp
        return {"status":"FIRST LOGIN OK"}

    if db[email] != fp:
        return {"status":"DEVICE MISMATCH"}

    return {"status":"LOGIN OK"}
