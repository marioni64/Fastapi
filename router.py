from typing import Annotated, List
from fastapi import APIRouter, Depends
from .SheMas import STask, STaskadd
from .repository import TasksRepository

router = APIRouter(
    prefix="/tasks"
)

@router.post("")
async def add_task(task: Annotated[STaskadd, Depends()]):

    task_id = await TasksRepository.add_one(task)
    return {
        "ok": True, "task_id": task_id
    }

@router.get("", response_model= List[STask])
async def get_tasks() -> List[STask]:
    tasks = await TasksRepository.find_all()
    return tasks