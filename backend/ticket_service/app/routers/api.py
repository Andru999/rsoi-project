from fastapi import APIRouter
from routers import manage, ticket

router = APIRouter()
router.include_router(ticket.router)
router.include_router(manage.router)
