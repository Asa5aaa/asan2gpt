from fastapi import FastAPI, Depends
from auth import router as auth_router
from admin import router as admin_router
from shutdown import check_shutdown
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def shutdown_middleware(request, call_next):
    if check_shutdown():
        return JSONResponse(status_code=503, content={"message": "AI SYSTEM OFF"})
    return await call_next(request)

app.include_router(auth_router)
app.include_router(admin_router)
