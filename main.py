from typing import Optional, Annotated
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from contextlib import asynccontextmanager

from .DateBase import create_tables, drop_tables
from .router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print("База очищена")
    await create_tables()
    print("База готова")
    yield
    print("Выкл")

app = FastAPI(lifespan = lifespan)
app.include_router(tasks_router)

class STaskadd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskadd):
    id: int







