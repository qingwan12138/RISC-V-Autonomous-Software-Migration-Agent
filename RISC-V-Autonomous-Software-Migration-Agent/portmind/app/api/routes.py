from fastapi import APIRouter
from app.agents.supervisor import SupervisorAgent

router = APIRouter()
supervisor = SupervisorAgent()

@router.post("/port")
def port_repo(repo_url: str, target: str = "riscv64-linux-gnu"):
    return supervisor.run(repo_url, target)
