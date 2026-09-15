from fastapi import APIRouter
router=APIRouter(prefix="/projects",tags=["projects"])
@router.get("")
def list_projects(): return [{"id":1,"name":"IPD测试项目","phase":"concept","status":"active"}]
@router.get("/{project_id}/phases")
def phases(project_id:int): return {"project_id":project_id,"phases":["concept","plan","develop","verify","release","lifecycle"]}
