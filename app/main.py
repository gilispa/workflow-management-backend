from fastapi import FastAPI
from app.api.v1.users import router as users_router

app = FastAPI(title="Workflow Management API")

app.include_router(users_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
