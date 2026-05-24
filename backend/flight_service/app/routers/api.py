from fastapi import APIRouter
from routers import airport, flight, manage

router = APIRouter()
router.include_router(flight.router)
router.include_router(airport.router)
router.include_router(manage.router)
