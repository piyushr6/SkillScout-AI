from fastapi import FastAPI
from routers import auth
from database import get_connection

app = FastAPI(
    title="SkillScout AI",
    description="AI-powered learning roadmap generator",
    version="0.1.0"
)

app.include_router(auth.router)

@app.get("/health")
def health_check():
    try:
        conn = get_connection()
        conn.close()
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}