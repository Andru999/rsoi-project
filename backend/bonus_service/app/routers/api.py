from fastapi import APIRouter
from routers import manage, privilege, privilege_history

router = APIRouter()
router.include_router(privilege.router)
router.include_router(privilege_history.router)
router.include_router(manage.router)
