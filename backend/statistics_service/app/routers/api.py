from fastapi import APIRouter
from routers import manage, statistics

router = APIRouter()
router.include_router(manage.router)
router.include_router(statistics.router)
