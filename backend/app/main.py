from fastapi import FastAPI
from .api.projects import router as projects_router
app=FastAPI(title="IPD研发项目管理系统 API",version="0.1.0")
app.include_router(projects_router,prefix="/api")
@app.get("/health")
def health(): return {"status":"ok","version":"0.1.0"}
