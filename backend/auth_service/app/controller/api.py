from controller import user
from fastapi import APIRouter

controller = APIRouter()
controller.include_router(user.controller)
